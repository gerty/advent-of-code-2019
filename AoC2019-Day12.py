# Code written by @gerty

# Input from Day 12, Problem 1 (and 2) of Advent of Code 2019
# Input files in same directory
# My input: in file Day09-INPUT.txt

xpoints = [3, 10, -3, -8]
ypoints = [-6, 7, -7, 0]
zpoints = [6, -9, 9, 4]
xvelocities = [0, 0, 0]
yvelocities = [0, 0, 0]
zvelocities = [0, 0, 0]
kenergy = 0
penergy = 0

# <x=3, y=-6, z=6>
# <x=10, y=7, z=-9>
# <x=-3, y=-7, z=9>
# <x=-8, y=0, z=4>

def calcVelocity(points, velocities):
    for i in points:
        velocities[i] = 0  # First set the velocity to zero
        for j in points:  # compare each point with all four points
            if points[j] > points[i]:  # gravitate in positive direction
                velocities[i] += 1
            if points[j] < points[i]:  # gravitate in negative direction
                velocities[i] -= 1

def addVelocity(points, velocities):
    for i in points:
        points[i] += velocities[i]

def calcEnergy(points, velocities):
    penergy = 0
    kenergy = 0
    for i in points:
        penergy += abs(points[i])
        kenergy += abs(velocities[i])
    return penergy * kenergy


for x in range(100):
     calcVelocity(xpoints, xvelocities)
     calcVelocity(ypoints, yvelocities)
     calcVelocity(zpoints, zvelocities)
     addVelocity(xpoints, xvelocities)
     addVelocity(ypoints, yvelocities)
     addVelocity(zpoints, zvelocities)

print("Ended up with " + str(calcEnergy(xpoints, xvelocities)) + "Energy in the x axis")
print("Ended up with " + str(calcEnergy(ypoints, yvelocities)) + "Energy in the y axis")
print("Ended up with " + str(calcEnergy(zpoints, zvelocities)) + "Energy in the z axis")

