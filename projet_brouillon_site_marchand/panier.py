from flask import Flask,render_template, request, redirect, url_for, flash
import os

panier= Flask(__name__)

panier.secret_key="panier"

@panier.route("/", methods=["GET"])
def home():
    return render_template("panier.html")

if __name__=="__main__":
    panier.run(debug=True, host="0.0.0.0", port=8000)
