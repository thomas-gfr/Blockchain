import hashlib
import os.path
import json


class Block:

    def __init__(self, base_hash: int, hash: str, parent_hash: str, transactions: []):
        self.base_hash = base_hash
        self.hash = hash
        self.parent_hash = parent_hash
        self.transactions = transactions

    def check_hash(self) -> bool:
        return hashlib.sha256(str(self.base_hash).encode()).hexdigest() == self.hash

    def add_transaction(self, wallet_emitter, wallet_receiver, amount):
        self.transactions.append({"emitter": wallet_emitter.unique_id,
                                  "receiver": wallet_receiver.unique_id,
                                  "sum": amount})

    def get_transaction(self, value):
        return self.transactions[value]

    def get_weight(self):
        return os.path.getsize("content/blocs/" + self.hash + ".json")

    def save(self):
        fichier = open("content/blocs/" + self.hash + ".json", "a")
        fichier.write(json.dumps(self.__dict__))
        fichier.close()

    def load(self, value):
        fichier = open("content/wallets/" + value + ".json", "r")
        file = json.load(fichier)
        fichier.close()
        self.base_hash = file["base_hash"]
        self.hash = file["hash"]
        self.parent_hash = file["parent_hash"]
        self.transactions = file["transactions"]
        # erreur si HASH existe pas
