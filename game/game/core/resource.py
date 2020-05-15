from .game_object import GameObject

class Resource(GameObject):
    def __init__(self, symbol='R'):
        super().__init__()
        self.symbol = symbol
