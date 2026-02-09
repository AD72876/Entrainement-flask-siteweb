"""from flask import Flask, render_template, request # Tu dis a python :"Je veux utiliser Flask,fonction render_template et fonction resquest dans mon programme"

app= Flask(__name__) #app le nom de mon site web. Flask(__name__) dit  a flask comment je vais trouver les fichier du projets.

Liste_message=[]# definir la liste qui stocke nos messages

@app.route("/") #Quand quelqu'un visite l'url de ton site web, ca va afficher la fonction qui se trouve juste en dessous en l'occurence home.

def home(): #Envoie le fichier html 'index' au naviguateur
	return render_template("index.html", messages=Liste_message)


@app.route("/add", methods=["POST"])
def add_message():
	message= request.form.get("message")
	if message:
		Liste_message.append(message)
	return render_template("index.html", messages=Liste_message)
app.run(debug=True) # ça demarre mon site localement ce qui me permet de modifier le site directement sur ma machine 
"""
"""
from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

Liste_message = []  # liste qui stocke les messages
i=0
@app.route("/")
def home():
    return render_template("index.html", messages=Liste_message)

@app.route("/add", methods=["POST"])   # <<< important
def add_message():
    message = request.form.get("username")
    password= request.form.get("password")
    global i
    exist=False
    for msg in Liste_message :
        if msg["username"]==message and msg["password"]==password:
            exist =True
            break

    if not exist:
        if message:
            if password:
                i=i+1
                Liste_message.append({
                    "numero": ("Donnée numéro", i),
                    "username": message,
                    "password": password,
                    "heure":datetime.now().strftime("%H:%M:%S")
                    })
    return render_template("index.html", messages=Liste_message)

@app.route("/supp", methods=["POST"])
def supprimer():
    numero= int(request.form.get("numero"))
    if numero:
        numero=int(numero)
        
        if 1<=numero<=len(Liste_message) !=0:
            Liste_message.pop(numero-1)
    return render_template("index.html", messages=Liste_message)

if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
"""


from flask import Flask, render_template, request
from datetime import datetime
app= Flask(__name__)


Liste_message=[] #Liste qui stockent les messages


@app.route("/")
def home():
    return render_template("index2.html", messages=Liste_message)


@app.route("/add", methods=["POST"])
def add_message():
    message=request.form.get("username")
    password=request.form.get("password")
    erreur=None

    if not message or not password :
        erreur="Message manquant"
        return render_template("index2.html", messages=Liste_message, error=erreur)
    
    for msg in Liste_message:
        if msg["username"]==message and msg["password"]==password:
            erreur="Doublon utilisateur/mot de passe existant"
            return render_template("index2.html",messages= Liste_message, error=erreur )
        
    succes="Vos données ont été enregistres"
    Liste_message.append({
        "numero": ("Données numéro",len(Liste_message)+1),
        "username": message,
        "password": password,
        "heure": datetime.now().strftime("%H:%M:%S")

        })
    return render_template("index2.html",messages=Liste_message,succes=succes)


@app.route("/supp", methods=["POST"])
def supp():
    longueur_liste=len(Liste_message)
    
    numero=request.form.get("numero")

    if numero :
        numero=int(numero)
        if  1 <= numero <= longueur_liste :
            Liste_message.pop(numero-1)
            return render_template("index2.html", messages=Liste_message)
        else:
            erreur="Veuillez rentrer un numéro valide"
            return render_template("index2.html",messages=Liste_message, error=erreur)
    else: 
        erreur="Veuillez rentrer un numéro"
        return render_template("index2.html",messages=Liste_message, error=erreur )


if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
