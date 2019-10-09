import heapq
from gridworld import gridworld
import pygame
import time
import random
from cell import cell

#sample grid from the description
grid = []
for row in range(101):
    grid.append([])
    for column in range(101):
        grid[row].append(0)

for raw in range(31):
    for colum in range(31):
        grid[random.randrange(0,100)][random.randrange(0,100)]=1
#initial status of observing blocks
visit = []
for row in range(101):
    visit.append([])
    for column in range(101):
        visit[row].append(0)
# grid = [[0, 0, 0, 0, 0],[0, 0, 1, 0, 0],[0, 0, 1, 1, 0],[0, 0, 1, 1, 0],[0, 0, 0, 1, 0]]
# visit = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
#manually setup start and end cells
start = cell(4, 2)
end = cell(90, 90)
start.getHeuristic(90, 90)
end.getHeuristic(90, 90)

gw = gridworld(605, 101, start, end, grid)
gw.draw()

#find the shortest path for each step
def computePath(curr, target):
    if curr.x == target.x and curr.y == target.y:
        return target
    closedset = set()
    direction = [[0,1],[1,0],[-1,0],[0,-1]]
    openlist = []
    heapq.heappush(openlist, curr)
    closedset.add((curr.x, curr.y))
    while len(openlist) != 0:
        pt = heapq.heappop(openlist)

        if pt.x == target.x and pt.y == target.y:
            # print("got it")
            return pt
            break
        for dir in direction:
            a = pt.x + dir[0]
            b = pt.y + dir[1]
            if a >= 0 and b >= 0 and a < len(visit) and b < len(visit[0]) and visit[a][b] == 0 and (a, b) not in closedset:
                # print(a, b)
                tmp = cell(a, b)
                closedset.add((a, b))
                tmp.parent = pt
                tmp.g = pt.g + 1
                tmp.getHeuristic(target.x, target.y)
                # print(tmp.f, tmp.g, tmp.h)
                heapq.heappush(openlist, tmp)
                # break
        # break
    return




#given the cell object, from the taget, find the next step
def getParent(a):
    future = []
    p = a.parent
    while p.parent != None:
        future.append(p)
        tmp = p
        p = p.parent
        tmp.parent = None
    return a.parent, future

#print out the path, for testing purpose
def result(path):
    string = ""
    for i in path:
        string += "("+str(i.x)+", "+str(i.y)+")"
    print(string)


#initial param for main loop
flag = False
pt = start
futurePath = []
path = []
while not flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = True
        continue

    #out print paths in the terminal for testing purpose
    # print("----------------------------------------------------")
    path.append(pt)
    # print("path: ")
    # result(path)
    # print("futurePath:")
    # result(futurePath)

    #draw the path
    gw.draw_cell([[path,2],[futurePath,3]],grid)

    #main algorithm
    direction = [[0,1],[1,0],[-1,0],[0,-1]]
    for dir in direction:
        a = pt.x + dir[0]
        b = pt.y + dir[1]
        if a >= 0 and b >= 0 and a < len(visit) and b < len(visit[0]) and grid[a][b] == 1:
            visit[a][b] = 1
    if len(futurePath) != 0 and visit[futurePath[0].x][futurePath[0].y] == 0:
        pt = futurePath[0]
        futurePath = futurePath[1:len(futurePath)]
    else:
        # print("need to computer a new path")
        # print(pt.x, pt.y)
        shortest = computePath(end, pt)
        # print(shortest.x,shortest.y)
        if shortest == None:
            print("fail to find a path")
            break
        if shortest.x == end.x and shortest.y == end.y:
            # print("finished")
            break
        nextPoint, futurePath = getParent(shortest)
        pt = nextPoint
        pt.parent = None
    if(pt.x == end.x and pt.y == end.y):
        print("reach the target")
        break
pygame.quit()
