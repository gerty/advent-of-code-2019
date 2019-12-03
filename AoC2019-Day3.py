# Code written by @gerty

# Input from Day 3, Problem 1 (and 2) of Advent of Code 2019
# Input files in same directory
# My input: in file Day03-INPUT.txt

with open('Day03-INPUT.txt', 'r') as f:
    filedata = f.readlines()

data = []
gridsize = 20000
origin = int(gridsize / 2);
grid = [[0 for i in range(gridsize)] for j in range(gridsize)]  # bits in grid locations will correspond to crossing
wirecode = 0  # keep track of which wire/bit we're tracking
minDistance = gridsize * 2

wire = filedata[0]
print(wire)
wirecode += 1
print(wirecode)
x = origin  # put the cursor at the origin (defined above as center-ish of grid) for each wire
y = origin
nav = wire.split(',')  # split commands by commas
print(nav)
movecount = 0

for navcom in nav:
    if navcom[0] == 'U':  # if the first letter of the navcom is an "UP" command
        for i in range(int(navcom[1:])):  # the remainder of the navcom is a distance
            y += 1  # go up
            movecount += 1
            if not (grid[x][y]):  # if the point has not been passed (only record first pass)
                grid[x][y] = movecount  # leave a trail of movecounts

    if navcom[0] == 'D':  # if the first letter of the navcom is an "UP" command
        for i in range(int(navcom[1:])):  # the remainder of the navcom is a distance
            y -= 1  # go down
            movecount += 1
            if not (grid[x][y]):  # if the point has not been passed
                grid[x][y] = movecount  # leave a trail of movecounts

    if navcom[0] == 'R':  # if the first letter of the navcom is an "UP" command
        for i in range(int(navcom[1:])):  # the remainder of the navcom is a distance
            x += 1  # go right
            movecount += 1
            if not (grid[x][y]):  # if the point has not been passed
                grid[x][y] = movecount  # leave a trail of movecounts

    if navcom[0] == 'L':  # if the first letter of the navcom is an "UP" command
        for i in range(int(navcom[1:])):  # the remainder of the navcom is a distance
            x -= 1  # go left
            movecount += 1
            if not (grid[x][y]):  # if the point has not been passed
                grid[x][y] = movecount  # leave a trail of movecounts

wire = filedata[1]
print(wire)
wirecode += 1
print(wirecode)
x = origin  # put the cursor at the origin (defined above as center-ish of grid) for each wire
y = origin
nav = wire.split(',')  # split commands by commas
print(nav)
movecount = 0

for navcom in nav:
    if navcom[0] == 'U':  # if the first letter of the navcom is an "UP" command
        for i in range(int(navcom[1:])):  # the remainder of the navcom is a distance
            y += 1
            movecount += 1  # if previous pass did not contact point just count and move along
            if (grid[x][y]):  # if record of a crossing at x,y then count it as a possible winner
                print('CROSSED at x:' + str(x) + " y:" + str(y) + " with moves: " + str(movecount + grid[x][y]))
                if movecount + grid[x][y] < minDistance:  # calculate Manhattan distance
                    minDistance = movecount + grid[x][y]
                    print(movecount + grid[x][y])
    if navcom[0] == 'D':  # if the first letter of the navcom is an "UP" command
        for i in range(int(navcom[1:])):  # the remainder of the navcom is a distance
            y -= 1
            movecount += 1  # if previous pass did not contact point just count and move along
            if (grid[x][y]):  # if record of a crossing at x,y then count it as a possible winner
                print('CROSSED at x:' + str(x) + " y:" + str(y) + " with moves: " + str(movecount + grid[x][y]))
                if movecount + grid[x][y] < minDistance:  # calculate Manhattan distance
                    minDistance = movecount + grid[x][y]
                    print(movecount + grid[x][y])
    if navcom[0] == 'R':  # if the first letter of the navcom is an "UP" command
        for i in range(int(navcom[1:])):  # the remainder of the navcom is a distance
            x += 1
            movecount += 1  # if previous pass did not contact point just count and move along
            if (grid[x][y]):  # if record of a crossing at x,y then count it as a possible winner
                print('CROSSED at x:' + str(x) + " y:" + str(y) + " with moves: " + str(movecount + grid[x][y]))
                if movecount + grid[x][y] < minDistance:  # calculate Manhattan distance
                    minDistance = movecount + grid[x][y]
                    print(movecount + grid[x][y])
    if navcom[0] == 'L':  # if the first letter of the navcom is an "UP" command
        for i in range(int(navcom[1:])):  # the remainder of the navcom is a distance
            x -= 1
            movecount += 1  # if previous pass did not contact point just count and move along
            if (grid[x][y]):  # if record of a crossing at x,y then count it as a possible winner
                print('CROSSED at x:' + str(x) + " y:" + str(y) + " with moves: " + str(movecount + grid[x][y]))
                if movecount + grid[x][y] < minDistance:  # calculate Manhattan distance
                    minDistance = movecount + grid[x][y]
                    print(movecount + grid[x][y])

# At this point we should have two (or more) wires overlayed onto our grid.
# Now we just need to find the closest intersecting point (all bits flipped) to our origin.
# Or not, if the above integrated code works.
print('DONE!')
print(minDistance)

# Not 12930 even when adding 2 to 12928 it is too low.