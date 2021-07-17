from KeyGen import KeyGen


class Encrypt:
    def __init__(self, content, binary=False):
        self.content = content
        self.binary = binary
        self.pubkey = KeyGen().get_public_key()
        self.get = self.encrypt(binary)

    def encrypt(self, binary):
        message = self.pubkey.encrypt(self.content)
        return bytes(message) if binary else str(message)
