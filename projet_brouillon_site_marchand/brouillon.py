from flask import Flask, render_template, request, redirect, url_for, flash
import os


brouillon= Flask(__name__)

brouillon.secret_key="brouillon"
def home():
    q=request.args.get

@brouillon.route("/", methods=["GET"])
def home():
    return render_template("brouillon.html")

if __name__== "__main__":
    brouillon.run(debug=True, host="0.0.0.0", port=8000)