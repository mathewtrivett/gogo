class Group:
    def __init__(self, colour, coordinates, groupId):
        self.colour = colour
        self.coordinates = [coordinates]
        self.id = groupID

    def mergeGroup(self, group):
        self.coordinates = self.coordinates + group.coordinates
