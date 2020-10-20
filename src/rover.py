from .planet import Planet


class Rover:

    global commands
    global vectors

    def __init__(self, x, y, orientation, planet):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.planet = planet

    # Movement functions
    def moveForward(self, vector):
        pass

    def moveBackward(self, vector):
        pass

    def moveLeft(self, vector):
        pass

    def moveRight(self, vector):
        pass

    # Rover commands
    commands = {
        'f': moveForward,
        'b': moveBackward,
        'l': moveLeft,
        'r': moveRight
    }

    # Movement vectors
    # Current orientation: [Distance x, Distance Y, Left, Right]
    vectors = {
        'N': [+0, +1, 'W', 'E'],
        'E': [+1, +0, 'N', 'S'],
        'W': [-1, +0, 'S', 'N'],
        'S': [+0, -1, 'E', 'W']
    }