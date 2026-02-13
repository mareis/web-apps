from flask import Flask, render_template, request, redirect

app = Flask(__name__)

navn = "Mads"

@app.route("/")
def hjem():
    return render_template("index.html", navn=navn)

@app.route("/om")
def om():
    return "Dette er meg og god helg."

@app.route("/gjest")
def gjest():
    gjestenavn = request.args.get("navn", "Ukjente")

    return render_template("gjest.html", navn=gjestenavn)

@app.route("/liste")
def liste():
    fruktfat = ["Druer🍇", "Bananer🍌", "Vannmeloner🍉", "Appelsiner🍊"] 

    return render_template("liste.html", fruktfat=fruktfat)


liste = []
@app.route("/handleliste", methods = ["GET", "POST"])
def handleliste():
    if request.method == "POST":
        ny_vare = request.form.get("nyVare")
        liste.append(ny_vare)

        return redirect("/handleliste")
    
    return render_template("handleliste.html", handleliste=liste)

    
if __name__ == "__main__":
    app.run(debug=True)