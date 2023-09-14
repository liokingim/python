import re
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

student_data = {
    1: {"name": "슈퍼맨", "score": {"국어": 90, "수학": 65}},
    2: {"name": "배트맨", "score": {"국어": 75, "영어": 80, "수학": 75}},
}


@app.route("/")
@app.route("/home")
def home():
    return "Hello, Flask!!!! "


@app.route("/user/<user_name>/<int:user_id>")
def user(user_name, user_id):
    return f"Hello, {user_name}({user_id})!"


@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()

    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content


@app.route("/student/<name>")
def index(name):
    return render_template("index.html", name=name)


@app.route("/student/<int:id>")
def student(id):
    return render_template(
        "student.html",
        template_name=student_data[id]["name"],
        template_score=student_data[id]["score"],
    )
