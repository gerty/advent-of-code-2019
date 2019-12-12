# Code written by @gerty

# Input from Day 9, Problem 1 (and 2) of Advent of Code 2019
# Input files in same directory
# My input: in file Day09-INPUT.txt

def computer(compData, inputparam):
    cycles = 1
    address = 0
    base = 0
    data = []
    for x in compData:
        data.append(int(x))
    for x in range(10000):
        data.append(0)
    # Using % and // (modulo and floor division to determine numeric values in ones, tens, hundreds, etc.
    while cycles > 0:
        opcode = data[address] % 100
        print("For cycle: " + str(cycles) +
              " Opcode: " + str(opcode) +
              " Address: " + str(address) +
              " Base: " + str(base))
        param = [0, 0, 0]  # This array will store the parameters after lookup but before assignment

        if opcode == 99:  # finish processing opcodes
            return data[0]  # data in location 0 is returned

        # Every opcode (other than 99) has one parameter
        if (data[address] % 1000) // 100 == 2:
            param[0] = data[data[address + 1]] + base  # relative mode (position + base)
        if (data[address] % 1000) // 100 == 1:
            param[0] = data[address + 1]  # immediate mode (parameter within instruction)
        if (data[address] % 1000) // 100 == 0:
            param[0] = data[data[address + 1]]  # position mode (parameter in referenced position)

        # these opcodes (1,2,5,6,7,8) use the second parameter
        if opcode == 1 or opcode == 2 or opcode == 5 or opcode == 6 or opcode == 7 or opcode == 8:
            if (data[address] % 10000) // 1000 == 2:
                param[1] = data[data[address + 2]] + base  # relative mode
            if (data[address] % 10000) // 1000 == 1:
                param[1] = data[address + 2]  # immediate mode
            if (data[address] % 10000) // 1000 == 0:
                param[1] = data[data[address + 2]]  # position mode

        # these opcodes (1,2,7,8) use third parameters ** Since 3rd parameter is output, only pass pointer **
        if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
            if data[address] // 10000 == 2:
                param[2] = address + 3 + base  # relative mode
            if data[address] // 10000 == 1:  # immediate mode should never happen here
                print("Immediate mode attempted for parameter write at address: " + str(address + 3))
            if data[address] // 10000 == 0:
                param[2] = address + 3  # position mode
        print("Parameters = " + str(param))

        if opcode == 1:  # ADDS parameter 1 to parameter 2 and puts in position for parameter 3
            data[param[2]] = param[0] + param[1]
            address += 4  # # instruction length (3) plus opcode

        if opcode == 2:  # MULTIPLIES parameter 1 with parameter 2 and puts answer in position for parameter 3
            data[param[2]] = param[0] * param[1]
            address += 4  # # instruction length (3) plus opcode

        if opcode == 3:  # assigns an input (passed via function) to position for parameter 1
            data[param[0]] = inputparam
            address += 2  # instruction length (1) plus opcode

        if opcode == 4:  # Outputs data from position pointed to in parameter 1
            print("Output: " + str(data[param[0]]))
            address += 2  # # instruction length (1) plus opcode

        if opcode == 5:  # JUMPS to parameter 2 if parameter 1 is TRUE
            if param[0]:
                address = param[1]  # address jumps
            else:
                address += 3  # instruction length (2) plus opcode

        if opcode == 6:  # JUMPS to parameter 2 if parameter 1 is FALSE
            if not param[0]:
                address = param[1]  # address jumps
            else:
                address += 3  # instruction length (2) plus opcode

        if opcode == 7:  # STORES '1' in parameter 3's position if parameter 1 is LESS THAN parameter 2
            if param[0] < param[1]:
                data[param[2]] = 1
            else:
                data[param[2]] = 0  # Otherwise it stores a "0" there
            address += 4  # instruction length (3) plus opcode

        if opcode == 8:  # STORES '1' in parameter 3's position if parameter 1 EQUALS parameter 2
            if param[0] == param[1]:
                data[param[2]] = 1
            else:
                data[param[2]] = 0  # Otherwise it stores a "0" there
            address += 4  # instruction length (3) plus opcode

        if opcode == 9:  # adjust relative BASE by number in parameter 1
            base += param[0]
            address += 2  # instruction length (1) plus opcode
        cycles += 1

with open('Day09-INPUT.txt', 'r') as f:
    filedata = f.readlines()
myData = []
for line in filedata:
    myData = line.split(',')

print(myData)
print("Final result in location 0 after running opcodes to completion: " + str(computer(myData, 5)))
