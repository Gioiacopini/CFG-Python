#import flask from flask library
from flask import Flask

#use flask() to create an app
app = Flask("my_first_app")

#this line makes the function capable of responding to requests
@app.route("/")
def say_hello():
    return "Hello World"

app.run(debug=True, host="0.0.0.0")
