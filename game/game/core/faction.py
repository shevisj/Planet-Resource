from .game_object import GameObject
from .board import Board
from .planet import Planet

class Faction(GameObject):
    def __init__(self, player, planet_args=None, board_args=None):
        self.player = player
        self.player.faction = self
        if planet_args is not None:
            self.add_planet(**planet_args)
        if board_args is not None and hasattr(self, 'planet'):
            self.add_board(**board_args)
        super(Faction).__init__()

    def add_planet(self, **kwargs):
        self.planet = Planet(self, **kwargs)
        self.player.planet = self.planet

    def add_board(self, **kwargs):
        self.board = Board(self, self.planet, **kwargs)
        self.planet.board = self.board
        self.board.planet = self.planet
        self.player.board = self.board
