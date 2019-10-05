import pygame

#create a gridworld
class gridworld:

    def __init__(self, screen_size, width, height, margin, start, target, grid):

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.YELLOW = (255, 255, 0)

        self.width = width
        self.height = height
        self.margin = margin
        self.color = self.WHITE

        pygame.init()

        self.size = (screen_size, screen_size)
        self.win = pygame.display.set_mode((500, 500))

        pygame.display.set_caption("A* Algorithm Pathfinder")

        self.clock = pygame.time.Clock()

        self.start = [start.x, start.y]
        self.target = [target.x, target.y]

        self.grid = grid

        self.win.fill(self.BLACK)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if [row, col] == self.start:
                    self.color = self.YELLOW
                elif [row, col] == self.target:
                    self.color = self.GREEN
                elif grid[row][col] == 1:
                    self.color = self.BLACK
                else:
                    self.color = self.WHITE
                pygame.draw.rect(self.win,
					self.color,
					[(self.margin + self.width)*col+self.margin,
					(self.margin + self.height)*row+self.margin,
					self.width,
					self.height])
        pygame.display.flip()

    def draw_cell(self, nodes, colval):
        for node in nodes:
            row = node.x
            column = node.y
            if colval == 1:
                color = self.BLACK
            elif colval == 2:
                color = self.YELLOW
            elif colval == 3:
                color = self.GREEN
            else:
                color = self.WHITE
            rect = pygame.draw.rect(self.win,
					color,
					[(self.margin + self.width)*column+self.margin,
					(self.margin + self.height)*row+self.margin,
					self.width,
					self.height])

    def show(self):
        pygame.display.flip()

    def loop(self):
        flag = False
        while flag == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = True
            self.clock.tick(60)
