# Flask Message Board

Mini application web developpée avec Flask permettant:
- d'ajouter des message
- de les afficher
- de les supprimer
- de les stocker dans un fichier JSON

## Technologies utilisées
- Python 3
- Flask
- HTML / CSS
- JSON

## Fonctionnalités
- Ajout de messages avec horodatage
- Validation des entrées
- Messages flash (erreurs / succès)
- Stockage persistant via JSON

## Hashage pour les mots de passe
- Stockage des mots de passes sous forme de hachés pour une meilleure sécurité 

## Installation (http://127.0.0.1:8000/)

```bash
git clone https://github.com/TON_PSEUDO/flask-message-board.git
cd flask-message-board
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app2.py
