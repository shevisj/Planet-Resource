#!/bin/python

class Planet(object):
    def __init__(faction='Planet Name',
                 starting_position=0,
                 rate=1,
                 solar_system_size=12):
        self.start_pos = self.current_pos = starting_position
        self.rate = rate

    def move_foreward():
        self.current_pos = (self.current_pos + selfrate) % self.solar_system_size
        return self.current_pos

    def move_backward():
        self.current_pos = (self.solar_system_size + 1 
                            if self.current_pos == 0 
                            else self.current_pos) - self.rate
        return self.current_pos

    def distance_from(target_pos):
        d = abs(self.current_pos - target_pos)
        
