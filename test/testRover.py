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

    def test_rover_move_command_list_one_string(self):
        TestRoverMovements().assert_rover_movement('E', list("ffrfflffl"), 14, 8, 'N')


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

    def assert_rover_moves_through_wrapping(self, x, y, orientation, keys, finalX, finalY):
        warpRover = planet.landARover(x, y, orientation)
        warpRover.move(list(keys))
        self.assertEqual(finalX, warpRover.x)
        self.assertEqual(finalY, warpRover.y)

    # Test Rover warp when moving forward
    def test_rover_wrap_north_move_forward(self):
        self.assert_rover_moves_through_wrapping(0, 2, 'N', "f", 0, 0)

    def test_rover_wrap_east_move_forward(self):
        self.assert_rover_moves_through_wrapping(2, 0, 'E', "f", 0, 0)

    def test_rover_wrap_west_move_forward(self):
        self.assert_rover_moves_through_wrapping(0, 0, 'W', "f", 2, 0)

    def test_rover_wrap_south_move_forward(self):
        self.assert_rover_moves_through_wrapping(0, 0, 'S', "f", 0, 2)

    # Test Rover warp when moving backward
    def test_rover_wrap_north_move_backward(self):
        self.assert_rover_moves_through_wrapping(0, 0, 'N', "b", 0, 2)

    def test_rover_wrap_est_move_backward(self):
        self.assert_rover_moves_through_wrapping(0, 0, 'E', "b", 2, 0)

    def test_rover_wrap_west_move_backward(self):
        self.assert_rover_moves_through_wrapping(2, 0, 'W', "b", 0, 0)

    def test_rover_wrap_southth_move_backward(self):
        self.assert_rover_moves_through_wrapping(0, 2, 'S', "b", 0, 0)


class TestRoverObscacles(unittest.TestCase):

    def setUp(self):
        global planet
        planet = Planet(20, 20)
        planet.setObstacle(8, 18)

    def assert_obstacle_is_encountered(self, x, y, orientation, key):
        obstacleRover = planet.landARover(x, y, orientation)
        with self.assertRaisesRegexp(ValueError, "Obstacle encountered in 8:18"):
            obstacleRover.move(list(key))

    # Encountering obstacles while moving forward
    def test_obstacle_moving_forward_east(self):
        self.assert_obstacle_is_encountered(7, 18, 'E', "f")

    def test_obstacle_moving_forward_north(self):
        self.assert_obstacle_is_encountered(8, 17, 'N', "f")

    def test_obstacle_moving_forward_west(self):
        self.assert_obstacle_is_encountered(9, 18, 'W', "f")

    def test_obstacle_moving_forward_south(self):
        self.assert_obstacle_is_encountered(8, 19, 'S', "f")

    # Encountering obstacles while moving forward
    def test_obstacle_moving_backward_east(self):
        self.assert_obstacle_is_encountered(9, 18, 'E', "b")

    def test_obstacle_moving_backward_north(self):
        self.assert_obstacle_is_encountered(8, 19, 'E', "b")

    def test_obstacle_moving_backward_west(self):
        self.assert_obstacle_is_encountered(7, 18, 'W', "b")

    def test_obstacle_moving_backward_south(self):
        self.assert_obstacle_is_encountered(8, 17, 'S', "b")

    # Stopping before the obstacle
    def test_path_stops_before(self):
        obstacleRover = planet.landARover(6, 17, 'E')
        with self.assertRaisesRegexp(ValueError, "Obstacle encountered in 8:18"):
            obstacleRover.move(list("fflf"))
        self.assertEqual(8, rover.x)
        self.assertEqual(17, rover.y)
