from game.core import Axial
from unittest import TestCase

AXIAL_TO_CUBE = [[None, None, (0, -2, 2), (0, -3, 3), (0, -4, 4)], 
                 [None, (1, -2, 1), (1, -3, 2), (1, -4, 3), (1, -5, 4)], 
                 [(2, -2, 0), (2, -3, 1), (2, -4, 2), (2, -5, 3), None], 
                 [(3, -3, 0), (3, -4, 1), (3, -5, 2), None, None]]

class AxialTest(TestCase):
    def test_axial_to_cube(self):
        for q in range(4):
            for r in range(5):
                if 1 < (q+r) < 6:
                    a = Axial(q, r)
                    cube = a.to_cube()
                    self.assertEqual(AXIAL_TO_CUBE[q][r], cube.to_tuple())
