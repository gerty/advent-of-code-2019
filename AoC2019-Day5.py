# Code written by @gerty

# Input from Day 5, Problem 1 (and 2) of Advent of Code 2019
# Input files in same directory
# My input: in file Day05-INPUT.txt


def computer(memory, inputparam):
    data = []  # create a list for use inside the function
    done = False
    for i in memory:
        data.append(int(i))  # build local list "data" with only the integer version of the parameter
    address = 0
    parameters = [0, 0, 0]

    while not done:
        opcode = data[address] % 100

        if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:  # these opcodes use 3 parameters as input
            if (data[address] % 1000) // 100:
                parameters[0] = data[address+1]  # immediate mode writes parameter from within instruction
            else:
                parameters[0] = data[data[address+1]]  # position mode writes parameter from referenced position

            if (data[address] % 10000) // 1000:
                parameters[1] = data[address+2]  # immediate mode
            else:
                parameters[1] = data[data[address+2]]  # position mode

            if data[address] // 10000:  # immediate mode should never happen here
                print("Immediate mode attempted for parameter write at address: " + str(address + 3))
            else:
                parameters[2] = data[address+3]  # use referenced address (parameter 3) for output (never immediate)

        if opcode == 5 or opcode == 6:  # these opcodes use 2 parameters as input
            if (data[address] % 1000) // 100:
                parameters[0] = data[address+1]  # immediate mode
            else:
                parameters[0] = data[data[address+1]]  # position mode

            if (data[address] % 10000) // 1000:
                print("Immediate mode attempted for parameter write! At address: " + str(address + 2))
            else:
                parameters[1] = data[data[address+2]]  # position mode

        if opcode == 1:  # ADDS parameter 1 to parameter 2 and puts in position for parameter 3
            data[parameters[2]] = parameters[0] + parameters[1]
            address += 4

        if opcode == 2:  # MULTIPLIES parameter 1 to parameter 2 and puts in position for parameter 3
            data[parameters[2]] = parameters[0] * parameters[1]
            address += 4

        if opcode == 3:  # assigns an input to the slot pointed to in parameter 1
            data[data[address+1]] = inputparam
            address += 2

        if opcode == 4:  # fetches data from the slot pointed to in parameter 1
            print("Output code: " + str(data[data[address+1]]))
            address += 2

        if opcode == 5:  # JUMPS to parameter 2 if parameter 1 is TRUE
            if parameters[0]:
                address = parameters[1]
            else:
                address += 3

        if opcode == 6:  # JUMPS to parameter 2 if parameter 1 is FALSE
            if not parameters[0]:
                address = parameters[1]
            else:
                address += 3

        if opcode == 7:  # STORES '1' in parameter 3's position if parameter 1 is LESS THAN parameter 2
            if parameters[0] < parameters[1]:
                data[parameters[2]] = 1
            else:
                data[parameters[2]] = 0
            address += 4

        if opcode == 6:  # STORES '1' in parameter 3's position if parameter 1 EQUALS parameter 2
            if parameters[0] == parameters[1]:
                data[parameters[2]] = 1
            else:
                data[parameters[2]] = 0
            address += 4

        if int(data[address]) == 99:
            return data[0]

myData = []

with open('Day05-INPUT.txt', 'r') as f:
    filedata = f.readlines()
for line in filedata:
    myData = line.split(',')

print(myData)
# print(computer(myData, 1))
print(computer(myData, 5))
