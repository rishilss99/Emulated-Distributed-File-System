import sys
from importlib_metadata import metadata
from flask import Flask, request, render_template

sys.path.insert(0, r'C:\Users\User\hello\DSCI551\Emulated-Distributed-File-System\src\mongodb')

from metadata import MongoMetadata

app = Flask(__name__) 

ACCEPTED_COMMANDS = ['mkdir', 'ls', 'rm', 'put', 'cat', 'rmdir']
 

@app.route('/', methods =["GET", "POST"])
def enter_commands():
    if request.method == "POST":
        command = request.form.get("command")
        metadata = MongoMetadata()
        commands_split = command.split(" ")
        if (len(commands_split) == 2) and commands_split[0] in ACCEPTED_COMMANDS:
            print("Entered command is correct which is: ", command)
            if commands_split[0] == "mkdir":
                metadata.mkdir(commands_split[1])
                return commands_split
        else:
            print("Not supported command")

    return render_template("index.html")
 
if __name__=='__main__':
   app.run(debug=True) # host:localhost, port:5000
