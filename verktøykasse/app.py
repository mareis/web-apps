from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def hjem():
    return render_template("index.html")

@app.route("/hund")
def hund():
    melding = ""

    if "alder" in request.args:
        try:
            tall = int(request.args.get("alder"))
            melding = f'{tall} menneskeår tilsvarer {7*tall} hundeår.'

        except ValueError:
            melding = "Husk å skrive inn tall"

    return render_template("hund.html", melding = melding)

@app.route("/sok")
def søk():
    spilliste = ["Skate", "Roblox", "Fortnite", "Minecraft", "Solitary", "Chess", "Sims", "GTA", "Counter Strike", "World of Worldcraft", "Tetris"]

    resultater = spilliste

    if "q" in request.args:
        søkeord = request.args.get("q")

        if søkeord:
            filtrert_liste = []
            for spill in spilliste:
                if søkeord.lower() in spill.lower():
                    filtrert_liste.append(spill)

            resultater = filtrert_liste


    return render_template("sok.html", resultater=resultater)



    




if __name__ == "__main__":
    app.run(debug=True)