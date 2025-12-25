from flask import Flask, render_template, request
app=Flask(__name__)
def hello():
    return "Hello!"
@app.route("/", methods=["GET", "POST"])
def home():
    marks={
        "John":45,
        "Saurabh": 99,
        "Sutanu": 98,
        "Jeet":100,
        "Snehasis":67
    }
    return render_template("jinja.html", marks=marks)
app.run(debug=True)

