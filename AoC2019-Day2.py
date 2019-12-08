# Code written by @gerty

# Input from Day 2, Problem 1 (and 2) of Advent of Code 2019
# Input files in same directory
# My input: in file Day02-INPUT.txt
# Spending some time cleaning it up before using it for future AoC 2019 days

item = 0
result = 0
myData = []


def computer(memory, noun, verb):
    data = []  # create a list for use inside the function
    done = False
    for i in memory:
        data.append(int(i))  # build local list "data" with only the integers
    data[1] = int(noun)  # initialize the intcode program with predetermined initial values
    data[2] = int(verb)  # all of data[] should be of type integer
    address = 0

    while not done:
        if int(data[address]) == 1:
            data[data[address+3]] = data[data[address+1]] + data[data[address+2]]
            address += 4

        if int(data[address]) == 2:
            data[data[address+3]] = data[data[address+1]] * data[data[address+2]]
            address += 4

        if int(data[address]) == 99:
            return data[0]


with open('Day02-INPUT.txt', 'r') as f:
    filedata = f.readlines()
for line in filedata:
    myData = line.split(',')
print("The answer to part 1 is: " + str(computer(myData, 12, 2)))

# Part 2 Follows.....
target = 19690720  # The targeted result

for x in range(100):  # Cycle through range of possible nouns and verbs
    for y in range(100):
        if computer(myData, x, y) == target:  # myData from previous file read, compare result of noun/verb to target
            print("The answer to part 2 is: " + str(x*100+y))
