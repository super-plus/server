import pgpy
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
from config import pgp
from api.OS.Linux import get_os_distribution_description
from datetime import timedelta


class KeyGen:
    def __init__(self):
        self.exp = self.__validate_exp__(pgp["KEY_EXP"])
        self.size = self.__validate_key_size__(pgp["SIZE"])
        self.algorithm = self.validate_algorithm(pgp["ALGORITHM"])
        self.name = get_os_distribution_description()
        self.key = self.generate_key()
        self.uid = self.generate_uid()
        self.pair = self.generate_private_key()

    @staticmethod
    def __allowed__():
        return {'RSAEncryptOrSign', 'ECDSA', 'DSA'}

    @staticmethod
    def __get_algorithm__attribute(algorithm):
        return getattr(PubKeyAlgorithm, algorithm)

    @staticmethod
    def __validate_key_size__(size):
        if isinstance(size, int) and size in [2048, 4096]:
            return size
        raise Exception("Key size must be either 2048 or 4096")

    @staticmethod
    def __validate_exp__(exp):
        if isinstance(exp, int) and exp > 0:
            return exp
        raise Exception("Expiration date must be a integer greater than zero.")

    def validate_algorithm(self, algorithm):
        for i in self.__allowed__():
            if algorithm.upper() == i:
                return self.__get_algorithm__attribute(i)
            elif algorithm in i:
                return self.__get_algorithm__attribute(i)
        raise Exception("Algorithm is invalid! Valid algorithms: " + str(self.__allowed__()))

    def generate_key(self):
        return pgpy.PGPKey.new(self.algorithm, self.size)

    def generate_uid(self):
        return pgpy.PGPUID.new(self.name)

    def generate_private_key(self):
        return self.key.add_uid(self.uid,
                                usage={KeyFlags.Sign, KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
                                hashes=[HashAlgorithm.SHA256, HashAlgorithm.SHA384, HashAlgorithm.SHA512,
                                        HashAlgorithm.SHA224],
                                ciphers=[SymmetricKeyAlgorithm.AES256, SymmetricKeyAlgorithm.AES192,
                                         SymmetricKeyAlgorithm.AES128],
                                compression=[CompressionAlgorithm.ZLIB, CompressionAlgorithm.BZ2,
                                             CompressionAlgorithm.ZIP, CompressionAlgorithm.Uncompressed],
                                key_expiration=timedelta(days=self.exp))

    def export_private_key(self, binary=False):
        return bytes(self.key) if binary else str(self.key)

    def export_public_key(self, binary=False):
        return bytes(self.key.pubkey) if binary else str(self.key.pubkey)

    def export_pair(self, binary=False):
        if binary:
            return {
                'PUBLIC': bytes(self.key.pubkey),
                'PRIVATE': bytes(self.key)
            }
        else:
            return {
                'PUBLIC': str(self.key.pubkey),
                'PRIVATE': str(self.key)
            }

    def get_public_key(self):
        return self.key.pubkey

    def get_private_key(self):
        return self.key

    def get_pair(self):
        return {
            'PUBLIC': self.key.pubkey,
            'PRIVATE': self.key
        }
