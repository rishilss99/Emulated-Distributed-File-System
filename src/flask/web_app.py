import sys
from importlib_metadata import metadata
from flask import Flask, request, render_template

sys.path.insert(0, r'C:\Users\User\hello\DSCI551\Emulated-Distributed-File-System\src\mongodb')  # To handle import of module metadata (temporary)

from metadata import MongoMetadata

app = Flask(__name__)

ACCEPTED_COMMANDS = ['mkdir', 'ls', 'rm', 'put', 'cat', 'rmdir']
metadata = MongoMetadata()

COMMAND_DICT = {"mkdir" : metadata.mkdir,
                "ls" : metadata.ls}

@app.route('/', methods =["GET", "POST"])
def enter_commands():
    if request.method == "POST":
        print(request, request.data, request.json)
        command = request.json.get("command")
        commands_split = command.split(" ")
        data = COMMAND_DICT.get(commands_split[0])(commands_split[1])
        if data is None:
            data = "Not supported command"
        elif type(data) != list:
            data = "Something went wrong"
        return {'response': data}

    return render_template("terminal.html")
 
if __name__=='__main__':
   app.run(debug=True) # host:localhost, port:5000
