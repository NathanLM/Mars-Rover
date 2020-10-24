import unittest
from src.planet import Planet


class TestRover(unittest.TestCase):

    def setUp(self):
        global rover
        rover = Planet(20, 20).landARover(10, 10, 'E')

    # Rover rotation
    def test_rover_turn_to_face_north(self):
        self.assert_rover_turn_in_the_right_direction('N')

    def test_rover_turn_to_face_east(self):
        self.assert_rover_turn_in_the_right_direction('E')

    def test_rover_turn_to_face_west(self):
        self.assert_rover_turn_in_the_right_direction('W')

    def test_rover_turn_to_face_south(self):
        self.assert_rover_turn_in_the_right_direction('S')

    def assert_rover_turn_in_the_right_direction(self, orientation):
        rover.turnToFaceDirection(orientation)
        self.assertEqual(orientation, rover.orientation)


class TestRoverCommandList(unittest.TestCase):

    def setUp(self):
        global rover
        rover = Planet(20, 20).landARover(10, 10, 'E')

    # Rover command list
    def test_rover_move_command_list(self):
        TestRoverMovements().assert_rover_movement('E', list("f" "f" "r" "f" "f" "l" "f" "f" "l"), 14, 8, 'N')


class TestRoverMovements(unittest.TestCase):

    def setUp(self):
        global rover
        rover = Planet(20, 20).landARover(10, 10, 'E')

    def assert_rover_movement(self, orientation, commands, finalX, finalY, finalOrientation):
        rover.turnToFaceDirection(orientation)
        rover.move(commands)
        self.assertEqual(finalX, rover.x)
        self.assertEqual(finalY, rover.y)
        self.assertEqual(finalOrientation, rover.orientation)

    # Movement while facing Est
    def test_rover_move_forward_est(self):
        self.assert_rover_movement('E', list("f"), 11, 10, 'E')

    def test_rover_move_backward_est(self):
        self.assert_rover_movement('E', list("b"), 9, 10, 'E')

    def test_rover_move_left_est(self):
        self.assert_rover_movement('E', list("l"), 10, 10, 'N')

    def test_rover_move_right_est(self):
        self.assert_rover_movement('E', list("r"), 10, 10, 'S')

    # Movement while facing West
    def test_rover_move_forward_west(self):
        self.assert_rover_movement('W', list("f"), 9, 10, 'W')

    def test_rover_move_backward_west(self):
        self.assert_rover_movement('W', list("b"), 11, 10, 'W')

    def test_rover_move_left_west(self):
        self.assert_rover_movement('W', list("l"), 10, 10, 'S')

    def test_rover_move_right_west(self):
        self.assert_rover_movement('W', list("r"), 10, 10, 'N')

    # Movement while facing South
    def test_rover_move_forward_south(self):
        self.assert_rover_movement('S', list("f"), 10, 9, 'S')

    def test_rover_move_backward_south(self):
        self.assert_rover_movement('S', list("b"), 10, 11, 'S')

    def test_rover_move_left_south(self):
        self.assert_rover_movement('S', list("l"), 10, 10, 'E')

    def test_rover_move_right_south(self):
        self.assert_rover_movement('S', list("r"), 10, 10, 'W')

    # Movement while facing North
    def test_rover_move_forward_north(self):
        self.assert_rover_movement('N', list("f"), 10, 11, 'N')

    def test_rover_move_backward_north(self):
        self.assert_rover_movement('N', list("b"), 10, 9, 'N')

    def test_rover_move_left_north(self):
        self.assert_rover_movement('N', list("l"), 10, 10, 'W')

    def test_rover_move_right_north(self):
        self.assert_rover_movement('N', list("r"), 10, 10, 'E')


class TestRoverWrapping(unittest.TestCase):

    def setUp(self):
        global planet
        planet = Planet(3, 3)

    # Test Rover warp when moving forward
    def test_rover_wrap_north_move_forward(self):
        warpRover = planet.landARover(0, 2, 'N')
        warpRover.move(list("f"))
        self.assertEqual(0, warpRover.y)

    def test_rover_wrap_east_move_forward(self):
        warpRover = planet.landARover(2, 0, 'E')
        warpRover.move(list("f"))
        self.assertEqual(0, warpRover.x)

    def test_rover_wrap_west_move_forward(self):
        warpRover = planet.landARover(0, 0, 'W')
        warpRover.move(list("f"))
        self.assertEqual(2, warpRover.x)

    def test_rover_wrap_south_move_forward(self):
        warpRover = planet.landARover(0, 0, 'S')
        warpRover.move(list("f"))
        self.assertEqual(2, warpRover.y)

    # Test Rover warp when moving backward
    def test_rover_wrap_north_move_backward(self):
        warpRover = planet.landARover(0, 0, 'N')
        warpRover.move(list("b"))
        self.assertEqual(2, warpRover.y)

    def test_rover_wrap_est_move_backward(self):
        warpRover = planet.landARover(0, 0, 'E')
        warpRover.move(list("b"))
        self.assertEqual(2, warpRover.x)

    def test_rover_wrap_west_move_backward(self):
        warpRover = planet.landARover(2, 0, 'W')
        warpRover.move(list("b"))
        self.assertEqual(0, warpRover.x)

    def test_rover_wrap_southth_move_backward(self):
        warpRover = planet.landARover(0, 0, 'S')
        warpRover.move(list("b"))
        self.assertEqual(0, warpRover.y)



class TestRoverObscacles(unittest.TestCase):

    def setUp(self):
        global rover
        rover = Planet(20, 20).landARover(10, 10, 'E')
