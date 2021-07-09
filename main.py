import settings.settings
from classes.block import Block
from classes.chain import Chain
from classes.wallet import Wallet


def main():

    wallet1 = Wallet()
    wallet1.balance = 300
    wallet1.save()
    wallet2 = Wallet()
    wallet2.balance = 500
    wallet2.save()

    #chain = Chain(0,0,"00","00",[{"base_hash": 41959,"hash": 41959,"parent_hash": 41959,"transactions":[{"transaction_id": 1,"emitter": "93b31fbe-08c9-49bc-abec-794e0a702863","receiver": "a82b9371-4260-48fe-87a4-4d4b4f7605d7","sum": 300}]},{"base_hash": 41959,"hash": 41959,"parent_hash": 41959,"transactions":[{ "transaction_id": 2,"emitter": "93b31fbe-08c9-49bc-abec-794e0a702863", "receiver": "a82b9371-4260-48fe-87a4-4d4b4f7605d7","sum": 300}]}])
    #chain.add_block()
    #print(chain.add_transaction("0000de6ea3db2896d6e427d9415dfb77f8388f8e0b6b04ba21a7ded25232c097",wallet1,wallet2,300))
    #print(chain.find_transaction(2))

    #wallet3 = Wallet()
    #wallet3.save()
    #wallet3.add_balance(343)

    #wallet4 = Wallet()
    #wallet4.save()
    #print(settings.settings.TOKEN)


if __name__ == "__main__":
    main()
