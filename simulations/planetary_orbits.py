#!/bin/python

def move_left(planet_idx, rate, solar_system_size=12):
    return (planet_idx + rate) % solar_system_size

def move_right(planet_idx, rate, solar_system_size=12):
    planet_idx = solar_system_size + 1 if planet_idx == 0 else planet_idx
    return planet_idx - rate

solar_system = [0]*12
