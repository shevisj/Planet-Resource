from .resources import Continuum, Food, Gorgonium, Iron, Lithium

# ============== GLOBAL SETTINGS ==============

SOLAR_SYSTEM_SIZE = 13

# ============== UNIT SETTINGS ==============

WORKER_ATTACK = 1
WORKER_DEFENSE = 1
WORKER_PRODUCTION = 5

COMBAT_ATTACK = 5
COMBAT_DEFENSE = 5
COMBAT_PRODUCTION = 3

HERO_ATTACK = 10
HERO_SPECIAL_ATTACK = 15
HERO_DEFENSE = 10
HERO_PRODUCTION = 1

# ============== FACTION SETTINGS ==============

# Board layout
"""
           / \     / \ 
         /     \ /     \ 
        |   1   |   2   |
        |       |       |
       / \     / \     / \ 
     /     \ /     \ /     \ 
    |   1   |   2   |   3   |
    |       |       |       |
   / \     / \     / \     / \ 
 /     \ /     \ /     \ /     \ 
|   4   |   5   |   6   |   7   |
|       |       |       |       |
 \     / \     / \     / \     /
   \ /     \ /     \ /     \ /
    |   8   |   9   |  10   |
    |       |       |       |
     \     / \     / \     /
       \ /     \ /     \ /
        |  11   |  12   |
        |       |       |
         \     / \     / 
           \ /     \ /
"""
# --------------    Zidaan    --------------
ZIDAAN_INITIAL_POSITION = -1 #  set to -1 for random initial position
ZIDAAN_ORBITAL_RATE = 1
ZIDAAN_RESOURCE_ALLOCATION = list({
    1: Continuum,
    2: Food,
    3: Gorgonium,
    4: Iron,
    5: Lithium,
    6: Iron,
    7: Continuum,
    8: Gorgonium,
    9: Lithium,
    10: Food,
    11: Iron,
    12: Food,
    13: Gorgonium,
    14: Lithium,
}.values())

# --------------    Hianth    --------------
HIANTH_INITIAL_POSITION = -1 #  set to -1 for random initial position
HIANTH_ORBITAL_RATE = 1
HIANTH_RESOURCE_ALLOCATION = list({
    1: Continuum,
    2: Food,
    3: Gorgonium,
    4: Iron,
    5: Lithium,
    6: Iron,
    7: Continuum,
    8: Gorgonium,
    9: Lithium,
    10: Food,
    11: Iron,
    12: Food,
    13: Gorgonium,
    14: Lithium,
}.values())

# --------------    Gorgon    --------------
GORGON_INITIAL_POSITION = -1 #  set to -1 for random initial position
GORGON_ORBITAL_RATE = 1
GORGON_RESOURCE_ALLOCATION = list({
    1: Continuum,
    2: Food,
    3: Gorgonium,
    4: Iron,
    5: Lithium,
    6: Iron,
    7: Continuum,
    8: Gorgonium,
    9: Lithium,
    10: Food,
    11: Iron,
    12: Food,
    13: Gorgonium,
    14: Lithium,
}.values())

# --------------    Frent    --------------
FRENT_INITIAL_POSITION = -1 #  set to -1 for random initial position
FRENT_ORBITAL_RATE = 1
FRENT_RESOURCE_ALLOCATION = list({
    1: Continuum,
    2: Food,
    3: Gorgonium,
    4: Iron,
    5: Lithium,
    6: Iron,
    7: Continuum,
    8: Gorgonium,
    9: Lithium,
    10: Food,
    11: Iron,
    12: Food,
    13: Gorgonium,
    14: Lithium,
}.values())

# --------------    Lithix    --------------
LITHIX_INITIAL_POSITION = -1 #  set to -1 for random initial position
LITHIX_ORBITAL_RATE = 1
LITHIX_RESOURCE_ALLOCATION = list({
    1: Continuum,
    2: Food,
    3: Gorgonium,
    4: Iron,
    5: Lithium,
    6: Iron,
    7: Continuum,
    8: Gorgonium,
    9: Lithium,
    10: Food,
    11: Iron,
    12: Food,
    13: Gorgonium,
    14: Lithium,
}.values())
