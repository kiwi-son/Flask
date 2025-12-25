from flask import Flask, request, render_template
app=Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="POST":
        with open("file.txt", "w") as f:
            f.write(f"The name is {request.form['name']} and mail id is {request.form['email']}")
    return render_template("contact.html")

app.run(debug="True")