#cell object definition
class cell:
    h = 0
    g = 0
    f = 0
    parent = None
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # compares the second value
    def __lt__(self, other):
        return (self.f, self.g) < (other.f, other.g)  #small g value
        # return self.f * 300 - self.g < other.f * 300 - other.g   #larger g value

    def getHeuristic(self, targetx, targety):
        self.h = abs(targetx - self.x) + abs(targety - self.y)
        self.f = self.h + self.g
