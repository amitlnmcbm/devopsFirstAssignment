from flask import Flask,jsonify,request
usersVote={}

app= Flask(__name__)

@app.route("/")
def home_action():
    return "Welcome to the App"

@app.route("/health")
def health_function():
    return "App is running"

@app.get("/vote/<name>")
def voting(name):
    allUsers = usersVote.keys()
    for user in allUsers:
        if user == name:
            usersVote[name] = int(usersVote[name]) + 1
            return "Successfully Voting Completed"
    usersVote[name] = 1
    return "Successfully Voting Completed for new user"

@app.get("/results")
def votingResult():
    if len(usersVote.keys()) == 0:
        return "Not vote has been casted"    
    return usersVote

if __name__ == "__main__":
    app.run(debug = True)