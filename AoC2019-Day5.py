# Code written by @gerty

# Input from Day 5, Problem 1 (and 2) of Advent of Code 2019
# Input files in same directory
# My input: in file Day05-INPUT.txt


def computer(memory, noun, verb, inputparam):
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

        if int(data[address]) == 3:
            data[data[address+1]] = data[inputparam]
            address += 2

        if int(data[address]) == 4:
            # outputparam = data[data[address+1]] # find a way to output param
            print(data[data[address+1]])
            address += 2

        if int(data[address]) == 99:
            return data[0]


myData = []


with open('Day02-INPUT.txt', 'r') as f:
    filedata = f.readlines()
for line in filedata:
    myData = line.split(',')

print(myData)
print(computer(myData, 12, 2, 1))

# Not 682644 (too low), not 7594646 (too high)