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

    def setObstacle(self, x, y):
        pass

