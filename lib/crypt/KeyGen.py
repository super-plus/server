from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
from config import pgp


class KeyGen:
    def __init__(self):
        self.exp = pgp["KEY_EXP"]
        self.key = self.get_key_algorithm(pgp["ALGORITHM"])

    @staticmethod
    def __allowed__():
        return {'RSAEncryptOrSign', 'ECDSA', 'DSA'}

    def get_key_algorithm(self, key):
        for i in self.__allowed__():
            if key in i:
                return i
