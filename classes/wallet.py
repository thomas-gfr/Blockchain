import uuid
import json


class Wallet:
    unique_id = ""
    balance = 0
    history = {}

    def generate_unique_id(self):
        self.unique_id = str(uuid.uuid4())

    # Ajouter verifications pour les autres wallet

    def add_balance(self, value):
        self.balance += value

    def sub_balance(self, value):
        self.balance -= value

    def send(self):
        pass

    def save(self):
        fichier = open("content/wallets/" + self.unique_id + ".json", "a")
        fichier.write(json.dumps(self.__dict__))
        fichier.close()
