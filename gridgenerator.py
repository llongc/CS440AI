import os
import random

# create a new directory if not exist
if not os.path.exists("girds"):
    os.mkdir("grids")
    print("Directory " , "grids" ,  " Created ")


#creating 50 randomly generated grid
for i in range(50):
    fileN = "grids/grid" + str(i)

    grid = []
    for row in range(101):
        grid.append([])
        for column in range(101):
            grid[row].append(0)

    for raw in range(54):
        for colum in range(54):
            grid[random.randrange(0,101)][random.randrange(0,101)]=1

    grid[100][100] = 0
    grid[0][0] = 0
    f = open(fileN, "w")
    for row in range(101):
        for column in range(101):
            f.write(str(grid[row][column]))
        f.write("\n")
    f.close()
