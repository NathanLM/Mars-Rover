from .rover import Rover


class Planet:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = set()
