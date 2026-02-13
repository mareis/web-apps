from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hjem():
    navn = request.args.get("navn", "ukjent")
    return render_template("index.html", navn = navn)

@app.route("/om")
def om():
    return render_template("om.html")

if __name__ == "__main__":
    app.run(debug=True)