

for line in filedata:
    data = line.split()
    for item in data:
        print(item)

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
        return (int(funcData[0]))
