from flask import Flask, request, render_template

app = Flask(__name__) 

ACCEPTED_COMMANDS = ['mkdir', 'ls', 'rm', 'put', 'cat', 'rmdir']
 

@app.route('/', methods =["GET", "POST"])
def enter_commands():
    if request.method == "POST":
        command = request.form.get("command")
        commands_split = command.split(" ")
        if (len(commands_split) == 2) and commands_split[0] in ACCEPTED_COMMANDS:
            print("Entered command is correct which is: ", command)
            return commands_split
        else:
            print("Not supported command")
    return render_template("index.html")
 
if __name__=='__main__':
   app.run(debug=True) # host:localhost, port:5000
