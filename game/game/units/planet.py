#!/usr/bin/env python

class Planet(object):
    def __init__(self,
                 name='Planet Name',
                 starting_position=0,
                 rate=1,
                 solar_system_size=12):
        self.name = name
        self.start_pos = self.current_pos = starting_position
        self.rate = rate
        self.solar_system_size = solar_system_size

    def increment_orbit(self):
        self.current_pos = (self.current_pos + self.rate) % self.solar_system_size
        return self.current_pos

    def decrement_orbit(self):
        self.current_pos = (self.solar_system_size + 1 
                            if self.current_pos == 0 
                            else self.current_pos) - self.rate
        return self.current_pos

    def distance_from(self, target_pos):
        i = (self.current_pos - target_pos) % self.solar_system_size
        j = (target_pos - self.current_pos) % self.solar_system_size
        return min(i, j)

