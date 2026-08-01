from flask import Flask

app= Flask(__name__)


@app.route("/")
def home_action():
    return "Welcome to the App"

@app.route("/health")
def health_function():
    return "App is running"

if __name__ == "__main__":
    app.run(debug = True)