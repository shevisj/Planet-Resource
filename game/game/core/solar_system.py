from .object import CoreObject
from .planet import Planet

class SolarSystem(CoreObject):
    def __init__(self,
                 size=12,
                 planets={}):
        super().__init__()
        self.size = size
        self.planets = planets

    def add_planet(self, planet: Planet):
        planet.solar_system_size = self.size
        self.planets[planet.name] = planet

    def remove_planet(self, planet_name: str):
        if planet_name not in self.planets:
            return False
        del self.planets[planet_name]
        return True

    def orbital_state(self):
        return {p.name: p.position for p in self.planets.values()}

    def increment_orbits(self, n=1):
        for p in self.planets.values():
            p.increment_orbit(n)
        return self.orbital_state()

    def decrement_orbits(self, n=1):
        for p in self.planets.values():
            p.decrement_orbit(n)
        return self.orbital_state()

    def distance_between(self, planet_name_a: str, planet_name_b: str):
        if planet_name_a not in self.planets:
            raise Exception(f"{planet_name_a} does not exist in this solar system")
        elif planet_name_b not in self.planets:
            raise Exception(f"{planet_name_b} does not exist in this solar system")
        return self.planets[planet_name_a].distance_from(self.planets[planet_name_b].position)
