import sys
from flask import Flask, request, render_template

sys.path.insert(0, r'C:\Users\User\hello\DSCI551\Emulated-Distributed-File-System\src\mongodb')  # To handle import of module metadata (temporary)

from metadata import MongoMetadata

app = Flask(__name__)

ACCEPTED_COMMANDS = ['mkdir', 'ls', 'rm', 'put', 'cat', 'rmdir']
metadata = MongoMetadata()

COMMAND_DICT = {"mkdir" : metadata.mkdir,
                "ls" : metadata.ls,
                "rm" : metadata.rm,
                "cat" : metadata.cat}

@app.route("/", methods=["GET"])
def landing_page():
    print("Welcome to the landing page")
    return render_template("landing_page.html")

@app.route('/terminal', methods =["GET", "POST"])
def enter_commands():
    if request.method == "POST":
        print(request, request.data, request.json)
        command = request.json.get("command")
        commands_split = command.split(" ")
        data = COMMAND_DICT.get(commands_split[0])(commands_split[1])
        if data is None:
            data = ["Not supported command"]
        elif type(data) != list:
            # data = ["Something went wrong"]
            print(data)
        return {'response': data}

    return render_template("terminal.html")

@app.route('/interface', methods =["GET", "POST"])
def userInterface():
    print('CHECKPOINT', request, request.method)
    if request.method == "POST":
        print(request, request.data, request.json)
        command = request.json.get("command")
        identifier = request.json.get("identifier")
        if identifier == "ls":
            if command == "root":
                cmd = "/"
                folders = metadata.ls(cmd)
            else:
                folders = metadata.ls(command)
            print(folders)
            return {"response" : folders}
        elif identifier == "mkdir":
            metadata.mkdir(command)
        elif identifier == "rm":
            metadata.rm(command)
            print("rm code to be executed here")

    return render_template("index.html")
 
if __name__=='__main__':
   app.run(debug=True) # host:localhost, port:5000
