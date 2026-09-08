from flask import Flask, render_template, request
from checker import check_strength, check_breach

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    strength = None
    feedback = None
    breach_result = None

    if request.method == "POST":
        password = request.form["password"]
        strength, feedback = check_strength(password)
        breach_result = check_breach(password)

    return render_template("index.html", strength=strength, feedback=feedback, breach_result=breach_result)

if __name__ == "__main__":
    app.run(debug=True)