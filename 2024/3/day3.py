# -*- coding: utf-8 -*-
"""
Advent of Code 2024

Day 3
"""

import time


####################################
## Part 1
####################################

startTime = time.time()

grid = []
with open('day3_data.txt', 'r') as file:
    for line in file:
        grid.append(str(line.split())[2:-2])
        
        
# print(grid)
        
ans1 = 0
ans2 = 0
mulStr = 'mul('
doStr = 'do()'
dontStr = 'don\'t()'

do = True


for a in grid:
    ind = 0
    while ind != -1:
        
        if do:
            # Look for dont
            dontInd = a.find(dontStr)
        else:
            # Look for do
            dontInd = a.find(doStr)
        
        ind = a.find(mulStr)
        
        # if found index happens first, flip the logic
        # print(dontInd, ind)
        if dontInd < ind and dontInd != -1:
            do = not do
            a = a[dontInd:]
            continue
        
        a = a[ind+4:]
        
        # Found mul( now look for comma
        comidx = a[:].find(',')
        try:
            num1 = int(a[:comidx])
        except:
            # Not a number break out
            print('Num 1 Bad!', a[:comidx])
            num1 = 0
            
        # Found, now look for (comma)
        backidx = a[comidx:].find(')')
        try:
            num2 = int(a[comidx+1:comidx+backidx])
        except:
            # Not a number break out
            print('Num 2 Bad! ', a[comidx+1:comidx+backidx])
            num2 = 0
        
        ans1 += num1 * num2
        if do:
            ans2 += num1 * num2
        
        # print(a[:ind+10])
        # print('Ind = ', ind)
        print('Num1 = ', num1, ', Num2 = ', num2)
        
    
print('Answer 1 = ', ans1)

####################################
## Part 2
####################################




print('Answer 2 = ', ans2)

endTime = time.time()
totalTime = endTime - startTime
print('Time = ', totalTime, ' sec')