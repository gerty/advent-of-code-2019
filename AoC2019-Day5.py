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
    param = [0, 0, 0]  # This array will store the parameters after lookup but before assignment

    while not done:
        opcode = data[address] % 100
#        print("This opcode is: " + str(opcode))
        if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:  # these opcodes use 3 parameters as input
            if (data[address] % 1000) // 100:
                param[0] = data[address + 1]  # immediate mode writes parameter from within instruction
            else:
                param[0] = data[data[address + 1]]  # position mode writes parameter from referenced position

            if (data[address] % 10000) // 1000:
                param[1] = data[address + 2]  # immediate mode
            else:
                param[1] = data[data[address + 2]]  # position mode

            if data[address] // 10000:  # immediate mode should never happen here
                print("Immediate mode attempted for parameter write at address: " + str(address + 3))
            else:
                param[2] = data[address + 3]  # referenced address (parameter 3) for output (never immediate)

        if opcode == 3 or opcode == 4:  # these opcodes use only 1 parameter as input
            if (data[address] % 1000) // 100:
                param[0] = address + 1  # immediate mode
            else:
                param[0] = data[address + 1]  # position mode

        if opcode == 5 or opcode == 6:  # these opcodes use 2 parameters as input`
            if (data[address] % 1000) // 100:
                param[0] = data[address + 1]  # immediate mode
            else:
                param[0] = data[data[address + 1]]  # position mode

            if (data[address] % 10000) // 1000:
                param[1] = data[address + 2]  # immediate mode
            else:
                param[1] = data[data[address + 2]]  # position mode
#        print("Parameters are: " + str(param))

        if opcode == 1:  # ADDS parameter 1 to parameter 2 and puts in position for parameter 3
            data[param[2]] = param[0] + param[1]
            address += 4

        if opcode == 2:  # MULTIPLIES parameter 1 with parameter 2 and puts answer in position for parameter 3
            data[param[2]] = param[0] * param[1]
            address += 4

        if opcode == 3:  # assigns an input (passed via function) to the slot pointed to in parameter 1
            data[param[0]] = inputparam
            address += 2

        if opcode == 4:  # fetches data from the slot pointed to in parameter 1
            print("Intermediate output: " + str(data[param[0]]))
            address += 2

        if opcode == 5:  # JUMPS to parameter 2 if parameter 1 is TRUE
            if param[0]:
                address = param[1]
            else:
                address += 3

        if opcode == 6:  # JUMPS to parameter 2 if parameter 1 is FALSE
            if not param[0]:
                address = param[1]
            else:
                address += 3

        if opcode == 7:  # STORES '1' in parameter 3's position if parameter 1 is LESS THAN parameter 2
            if param[0] < param[1]:
                data[param[2]] = 1
            else:
                data[param[2]] = 0  # Otherwise it stores a "0" there
            address += 4

        if opcode == 8:  # STORES '1' in parameter 3's position if parameter 1 EQUALS parameter 2
            if param[0] == param[1]:
                data[param[2]] = 1
            else:
                data[param[2]] = 0  # Otherwise it stores a "0" there
            address += 4

        if opcode == 99:
            return data[0]

myData = []

with open('Day05-INPUT.txt', 'r') as f:
    filedata = f.readlines()
for line in filedata:
    myData = line.split(',')

print(myData)
print("Final output: " + str(computer(myData, 5)))

# Part 2: 225 is too low, 773660 is the right answer!