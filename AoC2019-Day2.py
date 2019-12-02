# Code written by @gerty

# Input from Day 2, Problem 1 (and 2) of Advent of Code 2019
# Input files in same directory
# My input: in file Day02-INPUT.txt

with open('Day02-INPUT.txt', 'r') as f:
    filedata = f.readlines()

data = []
item = 0
index = 0
done = False
result = 0

for line in filedata:
    data = line.split(',')
    print(data)
    print(len(data))
    data[1] = '12'
    data[2] = '2'
    print(data)
    print(len(data))
    print("Starting: " + str(index))

while not done:
    if int(data[index+0]) == 1:
        result = int(data[int(data[index+1])]) + int(data[int(data[index+2])])
        data[int(data[index+3])] = result
        index += 4
        print(data)

    if int(data[index+0]) == 2:
        result = int(data[int(data[index+1])]) * int(data[int(data[index+2])])
        data[int(data[index+3])] = result
        index += 4
        print(data)

    if int(data[index+0]) == 99:
        print("The answer is: ")
        print(int(data[index+0]))
        print(data)
        done = True

# Solution to Part 1 left as-is due to not quite understanding how it happened.

# Part 2 Follows.....


myData = []
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
            print("The answer is: ")
            return(int(funcData[0]))

for x in range(100):
    for y in range(100):
        myData.clear()
        for line in filedata:
            myData = line.split(',')
        myData[1] = x
        myData[2] = y
        print(myData)
        print("Checking x = " + str(x) + " and y = " + str(y))
        if flightComp(myData) == target:
            print(x*100+y)
            sys.exit()


