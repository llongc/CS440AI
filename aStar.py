import pygame 

# Defining some color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Set dimension for each cell
WIDTH = 94
HEIGHT = 94
MARGIN = 5



# Creating a two dimensional array
grid = []
for row in range(5):
    grid.append([])
    for column in range(5):
        grid[row].append(0)

# Creating blockage
grid[1][2]=1
grid[2][2]=1
grid[3][2]=1
grid[2][3]=1
grid[3][3]=1
grid[4][3]=1

# Initialize pygame
pygame.init()

# Set window size
win = pygame.display.set_mode((500, 500))

# Set window caption
pygame.display.set_caption("A* Algorithm Pathfinder")

# loop flag
flag = False

# Used to determine how fast the screen updates
clock = pygame.time.Clock()

while not flag:
    # If user clicked exit, the loop will be terminated 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = True

    # Drawing the grid
    win.fill(BLACK)
    for row in range(5):
        for column in range(5):
            color = WHITE
            if grid[row][column] == 1:
                color = BLACK
            pygame.draw.rect(win,
            color,[(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    clock.tick(30)
    # Update the screen if there is anything new
    pygame.display.flip()

pygame.quit()