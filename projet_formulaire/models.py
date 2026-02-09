from datetime import datetime

class Message:
    def __init__(self, username, password,snap,numero , heure=None):
        self.username = username
        self.password = password
        self.snap=snap
        self.numero = numero
        self.heure = heure or datetime.now().strftime("%H:%M:%S")

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password, 
            "snap": self.snap,
            "numero": self.numero,
            "heure": self.heure,
        }
