# Code written by @gerty

# Input from Day 1, Problem 1 (and 2) of Advent of Code 2019
# Input files in same directory
# My input: in file Day01-INPUT.txt

with open('Day01-INPUT.txt', 'r') as f:
    filedata = f.readlines()

x = 0
data = []
item = 0
found = False
target = 33
answer = 0
fuel = 0

for line in filedata:
    data = line.split()
    for item in data:
        print(item)
        fuel = int(item)
        fuel = int((fuel / 3)) - 2
        while fuel > 0:
            answer += fuel
            fuel = int((fuel / 3))-2


print(answer)

# Not 15142376
