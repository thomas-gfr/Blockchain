from classes.wallet import Wallet


def main():
    wallet = Wallet()
    wallet.load("20eeba69-5ce0-4c99-85aa-52fee64b4d45")
    print(wallet.balance)


if __name__ == "__main__":
    main()
