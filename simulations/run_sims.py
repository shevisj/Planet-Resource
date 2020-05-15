import argparse

from board_demo import board_demo
from planetary_orbits import planetary_orbits

SIMS = {
    'board_demo': board_demo,
    'planetary_orbits': planetary_orbits,
}

parser = argparse.ArgumentParser(description='Run a simulation')
parser.add_argument('name', type=str, nargs='+',
                   help='the name of the simulation to run')

args = parser.parse_args()

sim_to_run = args.name[0]

if sim_to_run == "*":
    for s in SIMS.values():
        s()
else:
    if sim_to_run not in SIMS:
        raise Exception(f"No such simulation: {sim_to_run}")
    SIMS[sim_to_run]()
