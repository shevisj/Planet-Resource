from game import GameState
from game.units import Worker, Combat, Hero

def board_demo():
    gs = GameState()

    zidaan_player = gs.players['Zidaan']

    zidaan_player.create_unit(Worker, location=3)
    zidaan_player.create_unit(Worker, location=5)
    zidaan_player.create_unit(Combat, location=0)
    zidaan_player.create_unit(Combat, location=11)
    zidaan_player.create_unit(Hero, location=10)

    print("\n=============== BOARD DEMO ===============")
    print("\nZidaan Resource Layout")
    zidaan_player.board.display('resources')


    print("\nZidaan Unit Layout")
    zidaan_player.board.display('units')


    print("\nPlayer Resource Count BEFORE Gathering")
    zidaan_player.display_resource_count()

    print("\nPlayer Resource Count AFTER Gathering")
    zidaan_player.gather_resources()
    zidaan_player.display_resource_count()
    print("")
