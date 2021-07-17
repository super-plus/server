import pathlib


server = {
    'PORT': 9000,
    'HOST': "192.168.1.89",
    'DEBUG': True,
}

api = {
    'BASE': "/api/"
}

pgp = {
    'KEY_EXP': 14,
    'ALGORITHM': 'RSA',
    'SIZE': 4096,
    'PATH': pathlib.Path(__file__).parent.resolve()
}
