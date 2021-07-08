from classes.wallet import Wallet


def main():
    wallet = Wallet()
    wallet.generate_unique_id()
    wallet.add_balance(2000)
    wallet.sub_balance(200)
    wallet.save()


if __name__ == "__main__":
    main()
