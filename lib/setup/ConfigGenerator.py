import pathlib


class Setup:
    def __init__(self):
        self.path = pathlib.Path(__file__).parents[2]

