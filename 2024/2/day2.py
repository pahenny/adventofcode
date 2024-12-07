# -*- coding: utf-8 -*-
"""
Advent of Code 2024

Day 2
"""
import time


def levelChecker(numbers):
    ans1 = 0
    # do a row
    for a in numbers:
        if a[0] > a[1]:
            asc = False
        elif a[0] < a[1]:
            asc = True
    
        # comparison time
        for b in range(len(a)):
            # Skip index if dampin
            # print(b)
            # print(len(a))
            # print('ab ', a[b])
            # print('ab1 ', a[b+1])
            # print(dontdampAgainLOL)

            if asc:
                if 1 <= (a[b+1] - a[b]) <= 3:
                    # Good
                    pass
                    
                else:
                    # Bad
                    break
            else:
                if -3 <= (a[b+1] - a[b]) <= -1:
                    # Good
                    pass
                    
                else:
                    # Bad
                    break
            
            if b == len(a)-2:
                ans1 += 1
                break
    return ans1    

def levelChecker2(numbers):
    ans1 = 0
    # do a row
    for a in numbers:
        found = False
        
        for i in range(len(a)):
            if found:
                break
            
            testNumb = a[:i] + a[i+1:]
            
            if testNumb[0] > testNumb[1]:
                asc = False
            elif testNumb[0] < testNumb[1]:
                asc = True
        
            # comparison time
            for b in range(len(testNumb)):
                # Skip index if dampin
                # print(b)
                # print(len(testNumb))
                # print('ab ', testNumb[b])
                # print('ab1 ', testNumb[b+1])
                    
                if asc:
                    if 1 <= (testNumb[b+1] - testNumb[b]) <= 3:
                        # Good
                        pass
                        
                    else:
                        # Bad
                        break
                else:
                    if -3 <= (testNumb[b+1] - testNumb[b]) <= -1:
                        # Good
                        pass
                        
                    else:
                        # Bad
                        break
                
                if b == len(testNumb)-2:
                    ans1 += 1
                    found = True
                    break
    return ans1    


startTime = time.time()

## Part 1
numbers = []
with open('day2_data.txt', 'r') as file:
    for line in file:
        numbers.append([int(num) for num in line.split()])
        
    # print(numbers)

'''
The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
'''
ans1 = levelChecker(numbers)

print('Answer 1 = ', ans1)

## Part 2

ans2 = levelChecker2(numbers)

print('Answer 2 = ', ans2)

endTime = time.time()
totalTime = endTime - startTime
print('Time = ', totalTime, ' sec')