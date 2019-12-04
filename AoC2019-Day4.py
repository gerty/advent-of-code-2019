# Code written by @gerty

# Input from Day 4, Problem 1 (and 2) of Advent of Code 2019
# Input files in same directory
# My input: 146810-612564 (a range)

y = 146810
answer = 0
passok = False

for x in range(146810, 612564):
    numstr = str(x)
    tempchar = ''
    passok = False
    for c in range(len(numstr)-1):
        if numstr[c] == numstr[c+1]:
            passok = True
    for c in range(len(numstr)-1):
        if int(numstr[c]) > int(numstr[c+1]):
            passok = False
    if passok:
        answer += 1
print(answer)

# not 4729, 1777, 460 (for me), 461, 1748? YES!