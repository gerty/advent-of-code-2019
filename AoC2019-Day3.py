# Code written by @gerty

# Input from Day 3, Problem 1 (and 2) of Advent of Code 2019
# Input files in same directory
# My input: in file Day03-INPUT.txt

with open('Day03-INPUT.txt', 'r') as f:
    filedata = f.readlines()

# data = []
gridsize = 20000
origin = int(gridsize / 2);
grid = [[0 for i in range(gridsize)] for j in range(gridsize)] # bits in grid locations will correspond to wire crossed
wirecode = 0  # keep track of which wire/bit we're tracking
minDistance = gridsize * 2

for line in filedata:
    data = line.split()
    for wire in data:
        print(wire)
        wirecode += 1
        print(wirecode)
        x = origin  # put the cursor at the origin (defined above as center-ish of grid) for each wire
        y = origin
        nav = wire.split(',')  # split commands by commas
        print(nav)
        for navcom in nav:
            if navcom[0] == 'U':  # if the first letter of the navcom is an "UP" command
                for i in range(int(navcom[1:])):  # the remainder of the navcom is a distance
                    y += 1
                    if not (int(grid[x][y]) & wirecode):  # if wirecode bit not flipped yet
                        grid[x][y] ^= wirecode
                        if grid[x][y] == 3:  # replace with full & of max wirecode if problem goes in that direction...
                            print('CROSSED at x:' + str(x) + " y:" + str(y) + " at distance" + str(x+y))
                            if abs(x-origin) + abs(y-origin) < minDistance:  # calculate Manhattan distance
                                minDistance = abs(x-origin) + abs(y-origin)
                                print(minDistance)
            if navcom[0] == 'D':  # if the first letter of the navcom is an "UP" command
                for i in range(int(navcom[1:])):  # the remainder of the navcom is a distance
                    y -= 1
                    if (not (grid[x][y] & wirecode)):  # if wirecode bit not flipped yet
                        grid[x][y] ^= wirecode
                        if grid[x][y] == 3:  # replace with full & of max wirecode if problem goes in that direction...
                            print('CROSSED at x:' + str(x) + " y:" + str(y) + " at distance" + str(x+y))
                            if abs(x-origin) + abs(y-origin) < minDistance:  # calculate Manhattan distance
                                minDistance = abs(x-origin) + abs(y-origin)
                                print(minDistance)
            if navcom[0] == 'R':  # if the first letter of the navcom is an "UP" command
                for i in range(int(navcom[1:])):  # the remainder of the navcom is a distance
                    x += 1
                    if (not (grid[x][y] & wirecode)):  # if wirecode bit not flipped yet
                        grid[x][y] ^= wirecode
                        if grid[x][y] == 3:  # replace with full & of max wirecode if problem goes in that direction...
                            print('CROSSED at x:' + str(x) + " y:" + str(y) + " at distance" + str(x+y))
                            if abs(x-origin) + abs(y-origin) < minDistance:  # calculate Manhattan distance
                                minDistance = abs(x-origin) + abs(y-origin)
                                print(minDistance)
            if navcom[0] == 'L':  # if the first letter of the navcom is an "UP" command
                for i in range(int(navcom[1:])):  # the remainder of the navcom is a distance
                    x -= 1
                    if (not (grid[x][y] & wirecode)):  # if wirecode bit not flipped yet
                        grid[x][y] ^= wirecode  # flip a bit associated with that wirecode
                        if grid[x][y] == 3:  # replace with full & of max wirecode if problem goes in that direction...
                            print('CROSSED at x:' + str(x) + " y:" + str(y) + " at distance" + str(x+y))
                            if abs(x-origin) + abs(y-origin) < minDistance:  # calculate Manhattan distance
                                minDistance = abs(x-origin) + abs(y-origin)
                                print(minDistance)

# At this point we should have two (or more) wires overlayed onto our grid.
# Now we just need to find the closest intersecting point (all bits flipped) to our origin.
# Or not, if the above integrated code works.
print('DONE!')
print(minDistance)
