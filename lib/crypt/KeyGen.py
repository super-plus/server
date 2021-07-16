from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
from config import pgp


class KeyGen:
    def __init__(self):
        self.exp = self.__validate_exp__(pgp["KEY_EXP"])
        self.key = self.validate_algorithm(pgp["ALGORITHM"])

    @staticmethod
    def __allowed__():
        return {'RSAEncryptOrSign', 'ECDSA', 'DSA'}

    @staticmethod
    def __get_algorithm__attribute(key):
        return getattr(PubKeyAlgorithm, key)

    @staticmethod
    def __validate_exp__(exp):
        if isinstance(exp, int) and exp > 0:
            return exp
        raise Exception("Expiration date must be a integer greater than zero.")

    def validate_algorithm(self, key):
        for i in self.__allowed__():
            if key == i:
                return self.__get_algorithm__attribute(i)
            elif key in i:
                return self.__get_algorithm__attribute(i)
        raise Exception("Algorithm is invalid! Valid algorithms: " + str(self.__allowed__()))
