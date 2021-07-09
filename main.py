from classes.block import Block
from classes.chain import Chain
from classes.wallet import Wallet


def main():
    chain = Chain(0,0,"00","00",[{"base_hash": 270376, "hash": "0000d2ed5059b9f382f385b4d3c1f33ebbf5238ca9fe302270fee05985243319", "parent_hash": "00", "transactions": []}])

    print(chain.get_block("0000d2ed5059b9f382f385b4d3c1f33ebbf5238ca9fe302270fee05985243319"))

if __name__ == "__main__":
    main()
