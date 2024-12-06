# -*- coding: utf-8 -*-
"""
Advent of Code 2024

Day 6
"""

import time

'''
Return 1 on infinite loop
0 for a solve
'''
def guardMove(grid, mov, xpos, ypos, timeoutCnt=10000, rewrite=True):
    cnt = 0
    while True:
        # Index move
        if mov == 0:
            ypos -= 1
        elif mov == 1:
            xpos += 1
        elif mov == 2:
            ypos += 1
        elif mov == 3:
            xpos -= 1
            
        if xpos >= maxSize or ypos >= maxSize or xpos == -1 or ypos == -1:
            return 0
        
        # print('Loc (y,x) = ', ypos, ', ', xpos)
        if grid[ypos][xpos] != '#':
            if rewrite:
                grid[ypos] = grid[ypos][:xpos] + '0' + grid[ypos][xpos + 1:]
        else:
            # Undo the move
            if mov == 0:
                ypos += 1
            elif mov == 1:
                xpos -= 1
            elif mov == 2:
                ypos -= 1
            elif mov == 3:
                xpos += 1
                    
            # Hit the #, turn
            mov = (mov + 1) % 4
                       
        # Timeout count
        if cnt >= timeoutCnt:
            # print('We stuck boiz')
            return 1
        else:
            cnt += 1
            

####################################
## Part 1
####################################

startTime = time.time()

grid = []
with open('day6_data.txt', 'r') as file:
    for line in file:
        grid.append(str(line.split())[2:-2])

#print(grid[2][3])

# Find the ^<>V
for a in grid:
    for b in a:
        if b == '^':
            print('yo')
            yposSt = grid.index(a)
            xposSt = a.index(b)
        if b == '.':
            b = '0'
            
print('Loc = ', xposSt, ', ', yposSt)
# print(grid)

# We Movin
mov = 0
maxSize = len(grid[0])
# print('Max Size = ', maxSize)
xpos = xposSt
ypos = yposSt

guardMove(grid, mov, xpos, ypos)
print(grid)
        
# Count the 0s
cnt = 0
for a in grid:
    for b in a:
        if b == '0':
            cnt += 1
        
# Count the starting spot
cnt += 1
            
print('Answer 1 = ', cnt)

# Part 2

# Brute force try every square
xpos = xposSt
ypos = yposSt
ans2 = 0

for i in range(maxSize):
    for j in range(maxSize):
        # put that location as a # if not already
        if grid[i][j] == '#' or grid[i][j] == '.':
            # Do nothing
            pass
        else:
            # Change the location
            grid[i] = grid[i][:j] + '#' + grid[i][j + 1:]
            
            # Reinitialize Start
            mov = 0
            xpos = xposSt
            ypos = yposSt
            
            ans2 += guardMove(grid, mov, xpos, ypos, cnt*3, rewrite=False)
            
            # Change the grid location back
            grid[i] = grid[i][:j] + 'V' + grid[i][j + 1:]
        

print(grid)
print('Answer 2 = ', ans2)

endTime = time.time()
totalTime = endTime - startTime
print('Time = ', totalTime, ' sec')