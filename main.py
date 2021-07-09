import settings.settings
from classes.block import Block
from classes.chain import Chain
from classes.wallet import Wallet


def main():
    # BLOCK TEST
    # POUR TESTER JE VOUS INVITE A ENLEVER LE # DEVANT LA LIGNE EN QUESTION

    # --- WALLET --- #

    # création de wallet
    # wallet1 = Wallet()

    # ajout de solde au wallet
    # wallet1.balance = 300 # ou wallet1.add_balance(300) # ou wallet1.sub_balance(200)

    # sauvegarde du wallet
    # wallet1.save()

    # chargement du wallet
    # wallet1.load()
    # print(wallet1.unique_id) # -> exemple
    
    # --- BLOCK --- #  

    # création de 2 wallet pour essayer les différentes fonctions de block
    # wallet1 = Wallet()
    # wallet1.balance = 500
    # wallet1.save()

    # wallet2 = Wallet()
    # wallet2.balance = 500
    # wallet2.save()

    # création du block
    # block = Block(0,"00","00",[])

    # regarder si hash correct 
    # print(block.check_hash())

    # ajouter une transaction
    # block.add_transaction(0,wallet1,wallet2,200)

    # récupérer une transaction
    # print(block.get_transaction(0))
    
    # obtenir taille dun fichier 
    # print(block.get_weight(00))
    # fonction save & load pareil que dans wallet

    # --- CHAIN --- #  

    # création de chain
    # chain = Chain(0,0,"00","00",[])

    # générer hash rassemble create_hash and verify_hash
    # chain.generate_hash()

    # généré nouveau block
    # chain.add_block()

    # récupéré un block en fonction de son hash
    # print(chain.get_block("00"))

    # ajout transaction
    # print(chain.add_transaction("0000de6ea3db2896d6e427d9415dfb77f8388f8e0b6b04ba21a7ded25232c097",wallet1,wallet2,300))

    # trouver transaction en en ayant plusieurs, pour cela : 
    # création de chain avec plusieurs blocks
    # chain = Chain(0,0,"00","00",[{"base_hash": 41959,"hash": 41959,"parent_hash": 41959,"transactions":[{"transaction_id": 1,"emitter": "93b31fbe-08c9-49bc-abec-794e0a702863","receiver": "a82b9371-4260-48fe-87a4-4d4b4f7605d7","sum": 300}]},{"base_hash": 41959,"hash": 41959,"parent_hash": 41959,"transactions":[{ "transaction_id": 2,"emitter": "93b31fbe-08c9-49bc-abec-794e0a702863", "receiver": "a82b9371-4260-48fe-87a4-4d4b4f7605d7","sum": 300}]}]
    # print(chain.find_transaction(2))

    # récupéré dernier nombre de transaction
    # print(chain.get_last_transaction_number())

    # TESTEZ LA MISE EN PLACE DES TOKENS
    # wallet1 = Wallet()
    # wallet1.save()
    # wallet2 = Wallet()
    # wallet2.save()
    # wallet3 = Wallet()
    # wallet3.save()
    # wallet4 = Wallet()
    # wallet4.save()
    # print(settings.settings.TOKEN)


if __name__ == "__main__":
    main()
