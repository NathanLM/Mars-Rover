from .rover import Rover


class Planet:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = set()

    def landARover(self, x, y, orientation):
        return Rover(x, y, orientation, self)

    def wrap_x(self, x):
        return x % self.width

    def wrap_y(self, y):
        return y % self.height

    def getObstacleObject(self, x, y):
        return "{:d}:{:d}".format(x, y)

    def setObstacle(self, x, y):
        self.obstacles.add(self.getObstacleObject(x, y))

    def isObstacleAt(self, x, y):
        return self.getObstacleObject(x, y) in self.obstacles
