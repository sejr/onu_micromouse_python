class Cell:
    x = 0
    y = 0
    weight = 0

    # How should I approach the issue of cell walls?

    def __init__(self):
        self.weight = 0

    def get_weight(self):
        return self.weight

    def get_coordinates(self):
        return [self.x, self.y]