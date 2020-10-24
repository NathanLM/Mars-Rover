class Rover:

    global commands
    global vectors

    def __init__(self, x, y, orientation, planet):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.planet = planet

    # Movement functions
    def move(self, keys):
        for key in keys:
            self.executeMoveCommand(commands[key])

    def executeMoveCommand(self, command):
        vector = vectors[self.orientation]
        command(self, vector)

    def moveForward(self, vector):
        self.x = self.planet.wrap_x(self.x + vector[0])
        self.y = self.planet.wrap_y(self.y + vector[1])

    def moveBackward(self, vector):
        self.x = self.planet.wrap_x(self.x - vector[0])
        self.y = self.planet.wrap_y(self.y - vector[1])

    def moveLeft(self, vector):
        self.orientation = vector[2]

    def moveRight(self, vector):
        self.orientation = vector[3]

    def turnToFaceDirection(self, desiredOrientation):
        while self.orientation != desiredOrientation:
            self.moveLeft(vectors[self.orientation])

    commands = {
        'f': moveForward,
        'b': moveBackward,
        'l': moveLeft,
        'r': moveRight
    }
    # Rover commands

    # Movement vectors
    # Current orientation: [Distance x, Distance Y, Left, Right]
    vectors = {
        'N': [+0, +1, 'W', 'E'],
        'E': [+1, +0, 'N', 'S'],
        'W': [-1, +0, 'S', 'N'],
        'S': [+0, -1, 'E', 'W']
    }