from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import json
import os
from storage import charger_messages, sauvegarder_messages 
from models import Message
from werkzeug.security import generate_password_hash, check_password_hash
app3= Flask(__name__)
app3.secret_key = "cle-secrete"

FICHIER_storage="storage.py"



error_message=None  

Liste_message=charger_messages()

@app3.route("/", methods=["GET"])


def home():
    global error_message
    err = error_message
    error_message = None  # disparaît après affichage
    q=request.args.get("q","").lower()
    if q:
        messages_filtre=[
            msg for msg in Liste_message
            if q in msg["username"].lower()
        ]


    else:
        messages_tries=sorted(Liste_message,key=lambda msg: msg["heure"],reverse=True)
        messages_filtre=messages_tries

    

    return render_template("essau.html", messages=messages_filtre)



error_message=None
@app3.route("/add", methods=["POST"])
def add_message():
    global error_message

    message = request.form.get("username")
    password = request.form.get("mot_de_passe")
    password=generate_password_hash(password)
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
    
    nombre=len(Liste_message)
    message=Message(message, password,snap,nombre)
    Liste_message.append(message.to_dict())    
    flash("Message ajouté avec succès", "succes")
    
    sauvegarder_messages(Liste_message)

    return redirect(url_for("home"))


@app3.route("/supp", methods=["POST"])
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

@app3.route("/edit/<int:numero>")
def edit(numero):
    msg = Liste_message[numero - 1]
    return render_template("edit.html", msg=msg)

@app3.route("/update/<int:numero>", methods=["POST"])
def modifier(numero):
    nouveau=request.form.get("username")
    Liste_message[numero - 1]["username"]=nouveau
    sauvegarder_messages(Liste_message)
    flash("Message modifié", "succes")
    return redirect(url_for("home"))


if __name__== "__main__":
    app3.run(debug=True, host="0.0.0.0", port=8000)