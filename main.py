from classes.block import Block
from classes.wallet import Wallet


def main():
    wallet1 = Wallet()
    wallet1.generate_unique_id()
    wallet1.add_balance(200000)
    wallet1.save()
    wallet2 = Wallet()
    wallet2.generate_unique_id()
    wallet2.add_balance(200000)
    wallet2.save()

    block = Block()
    block.get_weight()


if __name__ == "__main__":
    main()
