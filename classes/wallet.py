import uuid


class Wallet:
    unique_id = ''

    def generate_unique_id(self):
        self.unique_id = uuid.uuid4()

    # Ajouter verifications pour les autres wallet
