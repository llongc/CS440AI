import heapq
from gridworld import gridworld
import pygame
import time
import random
from cell import cell



#sample grid from the description
#grid = []
#for row in range(101):
    #grid.append([])
    #for column in range(101):
        #grid[row].append(0)

#for raw in range(31):
    #for colum in range(31):
        #grid[random.randrange(0,100)][random.randrange(0,100)]=1
#initial status of observing blocks
#visit = []
#for row in range(101):
    #visit.append([])
    #for column in range(101):
       # visit[row].append(0)

# grid = [[0, 0, 0, 0, 0],[0, 0, 1, 0, 0],[0, 0, 1, 1, 0],[0, 0, 1, 1, 0],[0, 0, 0, 1, 0]]
# visit = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]

grid = []
with open('grids/grid5') as file:
    for line in file:
        line = line[:-1]
        k = [int(char) for char in line]
        grid.append(k)
visit = [[] for i in range(101)]
for i in range(101):
    visit[i] = [0 for i in range(101)]


#manually setup start and end cells
# start = cell(4, 2)
# end = cell(4, 4)
# start.getHeuristic(4, 4)
# end.getHeuristic(4, 4)
start = cell(0, 0)
end = cell(100, 100)
start.getHeuristic(100, 100)
end.getHeuristic(100, 100)

gw = gridworld(605, 101, start, end, grid)
gw.draw()

expandedCell = list()

def checkandremove(pt, openlist):
    # print(len(openlist))
    # print("-----")
    for i in range(len(openlist)):
        # print(i)
        if pt.x == openlist[i].x and pt.y == openlist[i].y:
            del openlist[i]
            break

#find the shortest path for each step
def computePath(curr, target):
    # print("11111")
    # print(target.x, target.y)
    closedset = set()
    direction = [[0,1],[1,0],[-1,0],[0,-1]]
    openlist = []
    heapq.heappush(openlist, curr)
    closedset.add((curr.x, curr.y))
    while len(openlist) != 0:

        pt = heapq.heappop(openlist)
        closedset.add((pt.x, pt.y))
        # print("expanding cell: ")
        # print(pt.x, pt.y, pt.f, pt.g)
        # print("-------")
        if pt.x == target.x and pt.y == target.y:
            return pt, closedset
            break
        for dir in direction:
            a = pt.x + dir[0]
            b = pt.y + dir[1]
            if a >= 0 and b >= 0 and a < len(visit) and b < len(visit[0]) and visit[a][b] == 0 and (a, b) not in closedset:

                tmp = cell(a, b)
                # closedset.add((a, b))
                checkandremove(tmp, openlist)
                tmp.parent = pt
                tmp.g = pt.g + 1
                tmp.getHeuristic(target.x, target.y)
                # print(tmp.x, tmp.y, tmp.f, tmp.g)
                heapq.heappush(openlist, tmp)
                # print(len(openlist))
    return None, None




#given the cell object, from the taget, find the next step
def getParent(a):
    future = []
    p = a
    if p.parent == None:
        return p, future
    while p.parent.parent != None:
        future.insert(0, p)
        tmp = p
        p = p.parent
        tmp.parent = None
    return p, future

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
# count = 0;
while not flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = True
        continue

    #out print paths in the terminal for testing purpose
    # print("----------------------------------------------------")
    # count+=1
    # print(str(count)+" :")
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
        shortest, closedSet_i = computePath(pt, end)
        print("^^^^^^^^^^^^^^^^^^")
        # print(type(list(closedSet_i)))
        if shortest == None:
            print("fail to find a path")
            break
        if len(closedSet_i)!=0:
            expandedCell.extend(list(closedSet_i).copy())
        # print(type(expandedCell))
        shortest, closeset_i = computePath(pt, end)

        nextPoint, futurePath = getParent(shortest)
        pt = nextPoint
        pt.parent = None
    if(pt.x == end.x and pt.y == end.y):
        print("reach the target")
        break
print("number of expanded cells: ", len(expandedCell))
pygame.quit()
