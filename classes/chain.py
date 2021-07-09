import hashlib
import os.path
from classes.block import Block


class Chain:

    def __init__(self, last_transaction_number: int, last_block_number: int, hash: str, parent_hash: str, blocks: []):
        self.blocks = blocks
        self.last_transaction_number = last_transaction_number
        self.hash = hash
        self.parent_hash = parent_hash
        self.last_block_number = last_block_number

    def generate_hash(self):
        number = 0
        block_hash = self.create_hash(number)
        while not self.verify_hash(block_hash):
            number += 1
            block_hash = self.create_hash(number)
        self.parent_hash = str(self.hash)
        self.last_block_number = number
        self.hash = block_hash

    def create_hash(self, number):
        return hashlib.sha256(f'{self.last_block_number}{self.hash}{number}'.encode()).hexdigest()

    @staticmethod
    def verify_hash(value):
        if not os.path.isfile("content/blocs/" + value + ".json") and value[:4] == "0000":
            return True
        else:
            return False

    def add_block(self):
        self.generate_hash()
        block = Block(self.last_block_number, self.hash, self.parent_hash, [])
        self.blocks.append(block)
        block.save()

    def get_block(self, value):
        for key in self.blocks:
            if key["hash"] == value:
                return key
        return "hash introuvable, veuillez vérifier le hash"

    def add_transaction(self, hash, wallet_emitter, wallet_receiver, amount):
        if os.path.isfile("content/wallets/" + wallet_emitter.unique_id + ".json"):
            if os.path.isfile("content/wallets/" + wallet_receiver.unique_id + ".json"):
                if wallet_emitter.balance >= amount:
                    if self.get_block(hash) != "hash introuvable, veuillez vérifier le hash":
                        block = self.get_block(hash)
                        block = Block(block["base_hash"], block['base_hash'], block['base_hash'], [])
                        block.add_transaction(wallet_emitter, wallet_receiver, amount)
                        wallet_emitter.sub_balance(amount)
                        wallet_receiver.add_balance(amount)
                    else:
                        return "Le block est introuvable, veuillez vérifier le hash."
                else:
                    return "La balance du wallet émetteur ne permet pas de faire la transaction. " \
                           "Le solde est insuffisant"
            else:
                return "Le wallet du récepteur est introuvable. Veuillez vérifier celui-ci."
        else:
            return "Le wallet émetteur est introuvable. Veuillez vérifier celui-ci."

    def find_transaction(self, transaction_id):
        for key in self.blocks:
            if key['transactions'][0]['transaction_id'] == transaction_id:
                return key
        return "id de transaction introuvable, veuillez vérifier le numéro"
