#import flask from flask library
from flask import Flask, render_template


#use flask() to create an app
app = Flask("my_first_app")

#this line makes the function capable of responding to requests
@app.route("/qwerty")
def say_hello():
    return render_template("index.html")

app.run(debug=True, host="0.0.0.0")
