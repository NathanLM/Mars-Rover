from .rover import Rover


class Planet:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = set()

    def landARover(self, x, y, orientation):
        return Rover(x, y, orientation, self)

    def wrapX(self, x):
        return x % self.width

    def wrapY(self, y):
        return y % self.height

    def setObstacle(self, x, y):
        self.obstacles.add((x, y))

    def isObstacleAt(self, x, y):
        return (x, y) in self.obstacles
