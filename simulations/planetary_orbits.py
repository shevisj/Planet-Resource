from game.core import SolarSystem
from itertools import combinations
from string import ascii_uppercase
from tqdm import tqdm
from pprint import pprint
from random import randint, seed
from time import time

from game.factions import FACTION_LIST

"""
Latest Simulation Report

Solar system size: 13
Number of planets: 5
Iteration count:   1000

Average overall distance: 3.2316

Average distance by planet:
{'Frent': 3.22975,
 'Gorgon': 3.232,
 'Hianth': 3.23225,
 'Lithix': 3.232,
 'Zidaan': 3.232}

Average distance by pair:
{'Frent-Lithix': 3.229,
 'Gorgon-Frent': 3.229,
 'Gorgon-Lithix': 3.234,
 'Hianth-Frent': 3.23,
 'Hianth-Gorgon': 3.233,
 'Hianth-Lithix': 3.233,
 'Zidaan-Frent': 3.231,
 'Zidaan-Gorgon': 3.232,
 'Zidaan-Hianth': 3.233,
 'Zidaan-Lithix': 3.232}
"""

SOLAR_SYSTEM_SIZE = 13
N_PLANETS = 5 # <= 5
N_ORBITAL_ITERATIONS = 1000
RANDOM_SEED = time()

seed(RANDOM_SEED)
ss = SolarSystem(size=SOLAR_SYSTEM_SIZE)
planet_names = list(map(lambda x: x.__name__, FACTION_LIST))[:min(N_PLANETS, 5)]
ids = []
id_map = {}
for i, n in enumerate(planet_names):
    uuid = ss.create_planet(n, rate=i+1, initial_position=randint(0, SOLAR_SYSTEM_SIZE-1))
    ids.append(uuid)
    id_map[uuid] = n

overall_ctr = 0
overall_distance = 0
planet_ctr = {id_map[n]: 0 for n in ids}
distance_by_planet = {id_map[n]: 0 for n in ids}
pair_ctr = {'-'.join([id_map[i] for i in n]): 0 for n in combinations(ids, 2)}
distance_by_pair = {'-'.join([id_map[i] for i in n]): 0 for n in combinations(ids, 2)}

for _ in tqdm(range(N_ORBITAL_ITERATIONS)):
    ss.increment_orbits()
    for x in list(combinations(ids, 2)):
        pair_key = '-'.join([id_map[i] for i in x])
        dist = ss.distance_between(x[0], x[1])
        overall_distance += dist
        distance_by_planet[id_map[x[0]]] += dist
        distance_by_planet[id_map[x[1]]] += dist
        distance_by_pair[pair_key] += dist
        overall_ctr += 1
        planet_ctr[id_map[x[0]]] += 1
        planet_ctr[id_map[x[1]]] += 1
        pair_ctr[pair_key] += 1

average_overall_distance = float(overall_distance) / float(overall_ctr)
average_distance_by_planet = {k: float(distance_by_planet[k])/float(planet_ctr[k]) for k in distance_by_planet}
average_distance_by_pair = {k: float(distance_by_pair[k])/float(pair_ctr[k]) for k in distance_by_pair}


print("\nSimulation Report\n")
print(f"Solar system size: {SOLAR_SYSTEM_SIZE}\nNumber of planets: {N_PLANETS}\nIteration count:   {N_ORBITAL_ITERATIONS}")
print(f"\nAverage overall distance: {average_overall_distance}")
print("\nAverage distance by planet:")
pprint(average_distance_by_planet, width=20)
print("\nAverage distance by pair:")
pprint(average_distance_by_pair, width=20)
print("\n")
