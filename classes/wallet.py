import os.path
import uuid
import json
import settings.settings


class Wallet:

    def __init__(self):
        if settings.settings.TOKEN < settings.settings.MAX_TOKEN_NUMBER:
            self.unique_id = self.generate_unique_id()
            self.balance = 0
            self.history = {}
            settings.settings.TOKEN += 100
        else:
            print('Nombre de token insuffisant')

    def generate_unique_id(self):
        self.unique_id = str(uuid.uuid4())
        # --- Check if file(unique_id) exist --- #
        while os.path.isfile("content/wallets/" + self.unique_id + ".json"):
            self.unique_id = str(uuid.uuid4())
        return self.unique_id

    def add_balance(self, value):
        self.balance += value
        self.save()

    def sub_balance(self, value):
        self.balance -= value
        self.save()

    def send(self):
        pass

    def save(self):
        fichier = open("content/wallets/" + self.unique_id + ".json", "w+")
        fichier.write(json.dumps(self.__dict__))
        fichier.close()

    def load(self, value):
        if os.path.isfile("content/wallets/" + value + ".json"):
            fichier = open("content/wallets/" + value + ".json", "r")
            file = json.load(fichier)
            fichier.close()
            self.unique_id = file["unique_id"]
            self.balance = file["balance"]
            self.history = file["history"]
        else:
            return "Le wallet est introuvable, veuillez vérifier le nom du wallet"
