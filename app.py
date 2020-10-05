from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        title="index"
        )

@app.route("/research", methods=["GET"])
def research():
    return render_template(
        "research.html",
        title="research"
        )

@app.route("/member", methods=["GET"])
def member():
    return render_template(
        "member.html",
        title="member"
        )

if __name__ == "__main__":
    app.run(debug=True)