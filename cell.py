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
        if self.f < other.f:
            return True
        elif self.f > other.f:
            return False
        else:
            self.h < other.h

    def getHeuristic(self, targetx, targety):
        self.h = abs(targetx - self.x) + abs(targety - self.y)
        self.f = self.h + self.g
