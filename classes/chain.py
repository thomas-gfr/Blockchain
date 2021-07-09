import hashlib
import os.path
from classes.block import Block


class Chain:

    def __init__(self):
        self.blocks = []
        self.last_transaction_number = 0
        self.hash = "00"
        self.parent_hash = "00"
        self.last_block_number = 0

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
        new_block = Block(self.last_block_number, self.hash, self.parent_hash, [])
        self.blocks.append(new_block)
        new_block.save()

    def get_block(self, value):
        return self.blocks[value]

    def add_transaction(self, value, wallet_emitter, wallet_receiver, amount):
        block = self.get_block(value)
        block.add_transaction(wallet_emitter, wallet_receiver, amount)

