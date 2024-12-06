# -*- coding: utf-8 -*-
"""
Advent of Code 2024

Day 1
"""

## Part 1

with open('day1_data.txt', 'r') as file:
    numbers = file.read().split()

numbers = [int(num) for num in numbers]

col1 = numbers[::2]
col2 = numbers[1::2]

# print(col1[1])
# print(col2[1])

col1.sort()
col2.sort()

dif = 0
for i in range(len(col1)):
    dif += abs(col1[i] - col2[i])
    
    
print('Answer 1 = ', dif)

## Part 2

col1 = numbers[::2]
col2 = numbers[1::2]

ans2 = 0
for n in col1:
    #print(n)
    ans2 += n * col2.count(n)
    
    
print('Answer 2 =', ans2)