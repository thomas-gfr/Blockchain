import hashlib
import os.path
import json
from classes.block import Block


class Chain:
    last_transaction_number = 0

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

    @staticmethod
    def get_block(value):
        path = 'content/blocks/' + value + '.json'
        if os.path.isfile(path):
            block = open(path, 'r')
            block = json.load(block)
            response = Block(
                block['base_hash'],
                block['hash'],
                block['parent_hash'],
                block['transactions']
            )
            return response
        return "hash introuvable, veuillez vérifier le hash"

    def add_transaction(self, hash, wallet_emitter, wallet_receiver, amount):
        if os.path.isfile("content/wallets/" + wallet_emitter.unique_id + ".json"):
            if os.path.isfile("content/wallets/" + wallet_receiver.unique_id + ".json"):
                if wallet_emitter.balance >= amount:
                    if self.get_block(hash) != "hash introuvable, veuillez vérifier le hash":
                        block = self.get_block(hash)
                        new_transaction = block.add_transaction(
                            wallet_emitter.unique_id,
                            wallet_receiver.unique_id,
                            amount,
                            self.last_transaction_number + 1
                        )
                        wallet_emitter.sub_balance(amount)
                        wallet_receiver.add_balance(amount)

                        if new_transaction is True:
                            block.save()
                            for element in self.blocks:
                                if element.hash == block.hash:
                                    self.blocks[self.blocks.index(element)] = block
                            self.last_transaction_number += 1

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
            if key['transactions'][0]['transaction_number'] == transaction_id:
                return key
        return "id de transaction introuvable, veuillez vérifier le numéro"

    def get_last_transaction_number(self):
        return self.last_transaction_number
