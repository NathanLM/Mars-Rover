from .rover import Rover


class Planet:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = set()

    def landARover(self, x, y):
        return Rover(x, y, 'E', self)
