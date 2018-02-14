from flask import Flask

app = Flask("my_first_app")

@app.route("/")
def say_hello():
    return "Hello World"

app.run(debug=True, host="0.0.0.0")
