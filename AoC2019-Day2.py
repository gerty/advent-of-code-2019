# Code written by @gerty

# Input from Day 2, Problem 1 (and 2) of Advent of Code 2019
# Input files in same directory
# My input: in file Day02-INPUT.txt
# Spending some time cleaning it up before using it for future AoC 2019 days

with open('Day02-INPUT.txt', 'r') as f:
    filedata = f.readlines()

item = 0
done = False
result = 0
myData = []

def intcode (initialMemory, noun, verb):
    data = []  # create a list for use inside the function
    for i in initialMemory:
        data.append(int(i))  # append only the integers
    data[1] = int(noun)  # initialize the intcode program with predetermined initial values
    data[2] = int(verb)  # all of data[] should be of type integer
    index = 0

    while not done:
        if int(data[index+0]) == 1:
            data[data[index+3]] = data[data[index+1]] + data[data[index+2]]
            index += 4

        if int(data[index+0]) == 2:
            data[data[index+3]] = data[data[index+1]] * data[data[index+2]]
            index += 4

        if int(data[index+0]) == 99:
            return(data[0])


for line in filedata:
    myData = line.split(',')
print("The answer ot part 1 is: " + str(intcode(myData,12,2)))

# Part 2 Follows.....

target = 19690720

def flightComp(funcData):
    donehere = False
    i = 0
    while not donehere:
        if int(funcData[i + 0]) == 1:
            result = int(funcData[int(funcData[i + 1])]) + int(funcData[int(funcData[i + 2])])
            funcData[int(funcData[i + 3])] = result
            i += 4

        if int(funcData[i + 0]) == 2:
            result = int(funcData[int(funcData[i + 1])]) * int(funcData[int(funcData[i + 2])])
            funcData[int(funcData[i + 3])] = result
            i += 4

        if int(funcData[i + 0]) == 99:
            return(int(funcData[0]))

for x in range(100):
    for y in range(100):
        myData.clear()
        for line in filedata:
            myData = line.split(',')
        myData[1] = x
        myData[2] = y
        if flightComp(myData) == target:
            print("The answer to part 2 is: " + str(x*100+y))
            exit()

