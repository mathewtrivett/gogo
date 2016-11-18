class Group:
    def __init__(self, colour, coordinates):
        self.colour = colour
        self.coordinates = [coordinates]

    def mergeGroup(self, group):
        self.coordinates = self.coordinates + group.coordinates