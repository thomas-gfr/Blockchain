import settings.settings
from classes.block import Block
from classes.chain import Chain
from classes.wallet import Wallet


def main():

    wallet1 = Wallet()
    wallet1.save()
    wallet2 = Wallet()
    wallet2.save()

    wallet3 = Wallet()
    wallet3.save()
    wallet3.add_balance(343)

    #wallet4 = Wallet()
    #wallet4.save()
    #print(settings.settings.TOKEN)


if __name__ == "__main__":
    main()
