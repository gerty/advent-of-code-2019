# Code written by @gerty

# Input from Day 12, Problem 1 (and 2) of Advent of Code 2019
# Input files in same directory
# My input: in file Day09-INPUT.txt
# Real input: <x=3, y=-6, z=6> +++ <x=10, y=7, z=-9> +++ <x=-3, y=-7, z=9> +++ <x=-8, y=0, z=4>
# Example 1: <x=-1, y=0, z=2> +++ <x=2, y=-10, z=-7> +++ <x=4, y=-8, z=8> +++ <x=3, y=5, z=-1>

points = [[3, -6, 6], [10, 7, -9], [-3, -7, 9], [-8, 0, 4]]  # real input
# points = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]  # example 1
velocities = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
iterations = 1000


def calcVelocity(p, v):
    for point in range(len(p)):  # One point at a time
        for xyz in range(len(p[point])):  # Look at all dimensions
            for compare in range(len(p)):
                if p[point][xyz] > p[compare][xyz]:  # gravitate in positive direction
                    v[point][xyz] = v[point][xyz] - 1
                if p[point][xyz] < p[compare][xyz]:  # gravitate in negative direction
                    v[point][xyz] = v[point][xyz] + 1

def addVelocity(p, v):
    for i in range(len(p)):
        for j in range(len(p[i])):
            p[i][j] += v[i][j]


def calcEnergy(p, v):
    penergy = 0
    kenergy = 0
    result = 0
    for i in range(len(p)):
        penergy = abs(p[i][0]) + abs(p[i][1]) + abs(p[i][2])
        print("penergy = " + str(penergy))
        kenergy = abs(v[i][0]) + abs(v[i][1]) + abs(v[i][2])
        print("kenergy = " + str(kenergy))
        result += penergy * kenergy
    return result


for x in range(iterations):
    print("Iteration #: " + str(x))
    print(points)
    calcVelocity(points, velocities)
    print(velocities)
    addVelocity(points, velocities)

print(points)
print("Ended up with " + str(calcEnergy(points, velocities)) +
      " energy after " + str(iterations) + " iterations.")

# 172 is too low
# 4876 is too low
# 29328 is too high
# 6849 is CORRECT!
