import os.path
import uuid
import json


class Wallet:

    def __init__(self):
        self.unique_id = ""
        self.balance = 0
        self.history = {}

    def generate_unique_id(self):
        self.unique_id = str(uuid.uuid4())
        # --- Check if file(unique_id) exist --- #
        while os.path.isfile("content/wallets/" + self.unique_id + ".json"):
            self.unique_id = str(uuid.uuid4())

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

    def load(self, value):
        fichier = open("content/wallets/" + value + ".json", "r")
        file = json.load(fichier)
        fichier.close()
        self.unique_id = file["unique_id"]
        self.balance = file["balance"]
        self.history = file["history"]
        # erreur si wallet existe pas
