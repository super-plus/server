from KeyGen import KeyGen


class Decrypt:
    def __init__(self, message):
        self.message = message
        self.private_key = KeyGen().get_private_key()
        self.get = self.decrypt()

    def decrypt(self):
        return self.message.decrypt()
