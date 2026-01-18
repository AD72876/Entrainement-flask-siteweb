from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import json
import os
from storage import charger_messages, sauvegarder_messages 
app2= Flask(__name__)
app2.secret_key = "cle-secrete"

FICHIER_storage="storage.py"



error_message=None  

Liste_message=charger_messages()

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
    sauvegarder_messages(Liste_message)

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


        sauvegarder_messages(Liste_message)
        return redirect(url_for("home"))
    else:
        flash("Numéro hors limite", "error")
        return redirect(url_for("home"))

if __name__== "__main__":
    app2.run(debug=True, host="0.0.0.0", port=5000)