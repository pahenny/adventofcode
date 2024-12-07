# -*- coding: utf-8 -*-
"""
Advent of Code 2024

Day 4
"""

import time


####################################
## Part 1
####################################

startTime = time.time()

grid = []
with open('day4_data.txt', 'r') as file:
    for line in file:
        grid.append(str(line.split())[2:-2])
        
# print(grid)

# search for the X, look in every direction

ans1 = 0
ans2 = 0
print(grid[-2][-2])

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'X':
            
            # Look around for M, 8 possible options
            for x in (-1, 0, 1):
                for y in (-1, 0, 1):
                    if 0 <= i+3*x < len(grid[0]) and 0 <= j+3*y < len(grid[0]):
                        if grid[i+x][j+y] == 'M':
                            # found M, keep looking in that direction
                            if grid[i+2*x][j+2*y] == 'A':
                                # found A
                                if grid[i+3*x][j+3*y] == 'S':
                                    # Found S, we gottem
                                    print('Index/Dir', i, j, x, y)
                                    ans1 += 1
           
print('Answer 1 = ', ans1)             
            
####################################
## Part 2
####################################
# Find an X of MAS
for i in range(len(grid)):
    for j in range(len(grid[0])):
        # Find the A first this time
        if grid[i][j] == 'A':
            print('A Index/Dir', i, j)
            
            # Look around for A, 2 possible options
            if 0 <= i+1 < len(grid[0]) and 0 <= j+1 < len(grid[0]) and \
               0 <= i-1 < len(grid[0]) and 0 <= j-1 < len(grid[0]):
                if (grid[i+1][j-1] == 'M' and grid[i-1][j+1] == 'S') or \
                   (grid[i+1][j-1] == 'S' and grid[i-1][j+1] == 'M'):
                        # print('MS1 Index/Dir', i, j)
                        # Found one MAS, check for other
                        if (grid[i+1][j+1] == 'M' and grid[i-1][j-1] == 'S') or \
                           (grid[i+1][j+1] == 'S' and grid[i-1][j-1] == 'M'):
                            # Found both
                            print('2 Index/Dir', i, j)
                            ans2 += 1
                                            
     
print('Answer 2 = ', ans2)                               
                                    
endTime = time.time()
totalTime = endTime - startTime
print('Time = ', totalTime, ' sec')