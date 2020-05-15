from .game_object import GameObject
from .planet import Planet
from .faction import Faction

class SolarSystem(GameObject):
    def __init__(self,
                 size=13,
                 planets={}):
        super().__init__()
        self.size = size
        self.planets = planets

    def create_planet(self, 
                      identifier: str,
                      **kwargs):
        kwargs['solar_system'] = self
        planet = Planet(identifier, **kwargs)
        self.planets[planet.uuid] = planet
        return planet.uuid

    def add_planet(self, planet: Planet):
        planet.solar_system = self
        self.planets[planet.uuid] = planet

    def remove_planet(self, identifier: str):
        if identifier not in self.planets:
            return False
        del self.planets[identifier]
        return True

    def orbital_state(self):
        return {str(p.faction): p.position for p in self.planets.values()}

    def increment_orbits(self, n=1):
        for p in self.planets.values():
            p.increment_orbit(n)
        return self.orbital_state()

    def decrement_orbits(self, n=1):
        for p in self.planets.values():
            p.decrement_orbit(n)
        return self.orbital_state()

    def distance_between(self, planet_id_a: str, planet_id_b: str):
        if planet_id_a not in self.planets:
            raise Exception(f"{planet_id_a} does not exist in this solar system")
        elif planet_id_b not in self.planets:
            raise Exception(f"{planet_id_b} does not exist in this solar system")
        return self.planets[planet_id_a].distance_from(self.planets[planet_id_b].position)
