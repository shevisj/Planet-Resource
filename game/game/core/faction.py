from .game_object import GameObject
from .board import Board
from .planet import Planet

class Faction(GameObject):
    def __init__(self, player, planet_args=None, board_args=None):
        super().__init__()
        self.player = player
        self.player.faction = self
        if planet_args is not None:
            self.planet = Planet(self, **planet_args)
            self.player.planet = self.planet
        if board_args is not None:
            self.board = Board(self, self.planet, **board_args)
            self.player.board = self.board
            if hasattr(self, 'planet'):
                self.planet.board = self.board
                self.board.planet = self.planet
