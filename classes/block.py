import hashlib
import os.path
import json
import uuid


class Block:

    def __init__(self, base_hash: int, hash: str, parent_hash: str, transactions: []):
        self.base_hash = base_hash
        self.hash = hash
        self.parent_hash = parent_hash
        self.transactions = transactions

    def check_hash(self) -> bool:
        return hashlib.sha256(str(self.base_hash).encode()).hexdigest() == self.hash

    def add_transaction(self, wallet_emitter, wallet_receiver, amount):
        transaction_id = int(uuid.uuid1())
        while transaction_id == self.transactions["transaction_id"]:
            transaction_id = int(uuid.uuid1())
        wallet_emitter.sub_balance(amount)
        wallet_emitter.save()
        wallet_receiver.add_balance(amount)
        wallet_receiver.save()
        self.transactions.append({"transaction_id": transaction_id,
                                  "emitter": wallet_emitter.unique_id,
                                  "receiver": wallet_receiver.unique_id,
                                  "sum": amount})
        self.save()

    def get_transaction(self, transaction_id):
        for key in self.transactions:
            if key["transaction_id"] == transaction_id:
                return key
        return "transaction introuvable, veuillez vérifier le numéro"

    def get_weight(self):
        return os.path.getsize("content/blocs/" + self.hash + ".json")

    def save(self):
        fichier = open("content/blocs/" + self.hash + ".json", "w+")
        fichier.write(json.dumps(self.__dict__))
        fichier.close()

    def load(self, value):
        if os.path.isfile("content/blocs/" + value + ".json"):
            fichier = open("content/blocs/" + value + ".json", "r")
            file = json.load(fichier)
            fichier.close()
            self.base_hash = file["base_hash"]
            self.hash = file["hash"]
            self.parent_hash = file["parent_hash"]
            self.transactions = file["transactions"]
        else:
            return "Le hash est introuvable, veuillez vérifier le hash"
