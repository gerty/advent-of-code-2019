# Code written by @gerty

# Input from Day 6, Problem 1 (and 2) of Advent of Code 2019
# Input files in same directory
# My input: in file Day06-INPUT.txt

def computer(data, inputparam):
    done = False
    address = 0
    base = 0
    param = [0, 0, 0]  # This array will store the parameters after lookup but before assignment

# Using % and // (modulo and floor division to determine numeric values in ones, tens, hundreds, etc.

    while not done:
        opcode = data[address] % 100
#        print("This opcode is: " + str(opcode))
        if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:  # these opcodes use 3 parameters as input
            if (data[address] % 1000) // 100 == 2:
                param[0] = data[data[address + 1] + base]  # relative mode (position + base)
            if (data[address] % 1000) // 100 == 1:
                param[0] = data[address + 1]  # immediate mode (parameter within instruction)
            if (data[address] % 1000) // 100 == 0:
                param[0] = data[data[address + 1]]  # position mode (parameter in referenced position)

            if (data[address] % 10000) // 1000 == 2:
                param[1] = data[data[address + 2] + base]  # position mode
            if (data[address] % 10000) // 1000 == 1:
                param[1] = data[address + 2]  # immediate mode
            if (data[address] % 10000) // 1000 == 0:
                param[1] = data[data[address + 2]]  # position mode

            if data[address] // 10000 == 2:
                param[2] = data[address + 3] + base  # relative mode
            if data[address] // 10000 == 1:  # immediate mode should never happen here
                print("Immediate mode attempted for parameter write at address: " + str(address + 3))
            if data[address] // 10000 == 0:
                param[2] = data[address + 3]  # position mode

        if opcode == 5 or opcode == 6:  # these opcodes use 2 parameters as input
            if (data[address] % 1000) // 100 == 1:
                param[0] = data[address + 1]  # immediate mode
            if (data[address] % 1000) // 100 == 0:
                param[0] = data[data[address + 1]]  # position mode

            if (data[address] % 10000) // 1000 == 1:
                param[1] = data[address + 2]  # immediate mode
            if (data[address] % 10000) // 1000 == 0:
                param[1] = data[data[address + 2]]  # position mode

        if opcode == 3 or opcode == 4 or opcode == 9:  # these opcodes use only 1 parameter as input
            if (data[address] % 1000) // 100 == 1:
                param[0] = address + 1  # immediate mode
            if (data[address] % 1000) // 100 == 0:
                param[0] = data[address + 1]  # position mode

#        print("Parameters are: " + str(param))

        if opcode == 1:  # ADDS parameter 1 to parameter 2 and puts in position for parameter 3
            data[param[2]] = param[0] + param[1]
            address += 4  # address increments length of instruction

        if opcode == 2:  # MULTIPLIES parameter 1 with parameter 2 and puts answer in position for parameter 3
            data[param[2]] = param[0] * param[1]
            address += 4  # address increments length of instruction

        if opcode == 3:  # assigns an input (passed via function) to position for parameter 1
            data[param[0]] = inputparam
            address += 2  # address increments length of instruction

        if opcode == 4:  # Outputs data from the slot pointed to in parameter 1
            print("Output: " + str(data[param[0]]))
            address += 2  # address increments length of instruction

        if opcode == 5:  # JUMPS to parameter 2 if parameter 1 is TRUE
            if param[0]:
                address = param[1]  # address jumps
            else:
                address += 3  # address increments length of instruction

        if opcode == 6:  # JUMPS to parameter 2 if parameter 1 is FALSE
            if not param[0]:
                address = param[1]  # address jumps
            else:
                address += 3  # address increments length of instruction

        if opcode == 7:  # STORES '1' in parameter 3's position if parameter 1 is LESS THAN parameter 2
            if param[0] < param[1]:
                data[param[2]] = 1
            else:
                data[param[2]] = 0  # Otherwise it stores a "0" there
            address += 4  # address increments length of instruction

        if opcode == 8:  # STORES '1' in parameter 3's position if parameter 1 EQUALS parameter 2
            if param[0] == param[1]:
                data[param[2]] = 1
            else:
                data[param[2]] = 0  # Otherwise it stores a "0" there
            address += 4  # address increments length of instruction

        if opcode == 9:  # adjust relative BASE by number in parameter 1
            base += param[0]
            address += 2  # address increments length of instruction

        if opcode == 99:  # finish processing opcodes
            done = True
            return data[0]  # data in location 0 is returned


myData = []

with open('Day05-INPUT.txt', 'r') as f:
    filedata = f.readlines()
for line in filedata:
    myData = line.split(',')

print(myData)
print("Final result in location 0 after running opcodes to completion: " + str(computer(myData, 5)))

# 773660 is the right answer to Day 5 (with an input of 5)