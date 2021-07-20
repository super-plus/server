import pathlib
import sys


class Setup:
    def __init__(self, arguments):
        self.path = pathlib.Path(__file__).parents[2] / "config.py"
        self.port = arguments[1]
        self.algorithm = "RSA" if arguments[2] == 1 else "ECDH"
        self.keysize = 4096 if arguments[3] == 1 else 2048
        self.exp = arguments[4]

    def generate(self):
        replacement = {
            "{{PORT}}": self.port,
            "{{ALGORITHM}}": "'" + self.algorithm + "'",
            "{{KEYSIZE}}": self.keysize,
            "{{EXP}}": self.exp,
        }
        data = self.path.read_text()
        for key in replacement:
            data = data.replace(key, str(replacement[key]))
        self.path.write_text(data)


if __name__ == "__main__":
    Setup(sys.argv).generate()
