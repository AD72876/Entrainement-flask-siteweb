from datetime import datetime

class Message:
    def __init__(self,snap, username, password,numero , heure=None):
        self.snap=snap
        self.numero = numero
        self.username = username
        self.password = password
        self.heure = heure or datetime.now().strftime("%H:%M:%S")

    def to_dict(self):
        return {
            "username": self.username,
            "snap": self.snap,
            "password": self.password, 
            "heure": self.heure,
            "numero": self.numero
        }
