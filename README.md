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

## Installation

```bash
git clone https://github.com/TON_PSEUDO/flask-message-board.git
cd flask-message-board
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
