from game.core import Planet
from game.core.solar_system import SolarSystem
from itertools import combinations
from string import ascii_uppercase
from tqdm import tqdm
from pprint import pprint
from random import randint, seed
from time import time

"""
Latest Simulation Report

Solar system size: 13
Number of planets: 4
Iteration count:   1000

Average overall distance: 3.2303333333333333

Average distance by planet:
{'A': 3.231,
 'B': 3.2306666666666666,
 'C': 3.228666666666667,
 'D': 3.231}

Average distance by pair:
{'A-B': 3.232,
 'A-C': 3.228,
 'A-D': 3.233,
 'B-C': 3.229,
 'B-D': 3.231,
 'C-D': 3.229}
"""

SOLAR_SYSTEM_SIZE = 13
N_PLANETS = 4
N_ORBITAL_ITERATIONS = 1000
RANDOM_SEED = time()

seed(RANDOM_SEED)
ss = SolarSystem(size=SOLAR_SYSTEM_SIZE)
planet_names = list(ascii_uppercase)[:N_PLANETS]
for i, n in enumerate(planet_names):
    p = Planet(name=n, rate=i+1, initial_position=randint(0, SOLAR_SYSTEM_SIZE-1))
    ss.add_planet(p)

overall_ctr = 0
overall_distance = 0
planet_ctr = {n: 0 for n in planet_names}
distance_by_planet = {n: 0 for n in planet_names}
pair_ctr = {'-'.join(n): 0 for n in combinations(planet_names, 2)}
distance_by_pair = {'-'.join(n): 0 for n in combinations(planet_names, 2)}

for _ in tqdm(range(N_ORBITAL_ITERATIONS)):
    ss.increment_orbits()
    for x in list(combinations(planet_names, 2)):
        pair_key = '-'.join(x)
        dist = ss.distance_between(x[0], x[1])
        overall_distance += dist
        distance_by_planet[x[0]] += dist
        distance_by_planet[x[1]] += dist
        distance_by_pair[pair_key] += dist
        overall_ctr += 1
        planet_ctr[x[0]] += 1
        planet_ctr[x[1]] += 1
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
