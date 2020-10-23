import unittest
from src.rover import Rover
from src.planet import Planet


class TestRover(unittest.TestCase):


    def setUp(self):
        global rover
        rover = Planet(20, 20).landARover()

    # Test Rover movements

    def test_rover_move_command_list(self):
        rover.move(list("f" "f" "r" "f" "f" "l" "f" "f" "l"))
        self.assertEqual(14, rover.x)
        self.assertEqual(8, rover.y)
        self.assertEqual('N', rover.orientation)

    def test_rover_move_forward(self):
        rover.move(list("f"))
        self.assertEqual(11, rover.x)
        self.assertEqual(10, rover.y)
        self.assertEqual('E', rover.orientation)

    def test_rover_move_backward(self):
        rover.move(list("b"))
        self.assertEqual(9, rover.x)
        self.assertEqual(10, rover.y)
        self.assertEqual('E', rover.orientation)

    def test_move_left(self):
        rover.move(list('l'));
        self.assertEqual('N', rover.orientation)

    def test_rover_move_right(self):
        rover.move(list('r'))
        self.assertEqual('S', rover.orientation)
