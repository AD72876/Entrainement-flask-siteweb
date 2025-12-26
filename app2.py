from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import json
import os
app2= Flask(__name__)
app2.secret_key = "cle-secrete"



error_message=None


FICHIER_JOHNSON="messages.json"
if os.path.exists(FICHIER_JOHNSON):
    with open(FICHIER_JOHNSON, "r", encoding="utf-8") as popo:
        Liste_message=json.load(popo)
else:
    Liste_message=[]


def sauvegarder_messages():
    with open("messages.json", "w", encoding="utf-8") as f:
            json.dump(Liste_message, f, indent=4, ensure_ascii=False)

@app2.route("/")


def home():
    global error_message
    err = error_message
    error_message = None  # disparaît après affichage
    return render_template("essau.html", messages=Liste_message)



error_message=None
@app2.route("/add", methods=["POST"])
def add_message():
    global error_message

    message = request.form.get("username")
    password = request.form.get("mot_de_passe")
    date_anniv= request.form.get("date_anniversaire")
    snap= request.form.get("snap")
    if not message or not password or not date_anniv:
        succes=False
        flash("Données manquant", "error")
        return redirect(url_for("home"))

    for msg in Liste_message:
        if msg["username"] == message and msg["password"] == password:
            #error_message = "Doublon utilisateur/mot de passe existant"
            flash("Message doublon", "error")
            return redirect(url_for("home"))
        
    flash("Message ajouté avec succès", "succes")
    Liste_message.append({
        "nombre": len(Liste_message) + 1,
        "username": message,
        "password": password,
        "date_anniversaire":date_anniv,
        "snap": snap,
        "heure": datetime.now().strftime("%H:%M:%S")
    })
    sauvegarder_messages()

    return redirect(url_for("home"))


@app2.route("/supp", methods=["POST"])
def supp():
    global error_message

    numero = request.form.get("numero")

    if not numero or not numero.isdigit():
        flash("Veuillez rentrer un numéro valide", "error")
        return redirect(url_for("home"))

    numero = int(numero)

    if 1 <= numero <= len(Liste_message):
        Liste_message.pop(numero - 1)
        error_message = None

        # Re-numérotation propre
        for i, msg in enumerate(Liste_message):
            msg["numero"] = i + 1

        sauvegarder_messages()
        return redirect(url_for("home"))
    else:
        flash("Numéro hors limite", "error")
        return redirect(url_for("home"))

if __name__== "__main__":
    app2.run(debug=True, host="0.0.0.0", port=8000)