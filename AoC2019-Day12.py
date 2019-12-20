# Code written by @gerty

# Input from Day 12, Problem 1 (and 2) of Advent of Code 2019
# Input files in same directory
# My input: in file Day09-INPUT.txt
# Real input: <x=3, y=-6, z=6> +++ <x=10, y=7, z=-9> +++ <x=-3, y=-7, z=9> +++ <x=-8, y=0, z=4>
# Example 1: <x=-1, y=0, z=2> +++ <x=2, y=-10, z=-7> +++ <x=4, y=-8, z=8> +++ <x=3, y=5, z=-1>

import numpy as np

points = np.array([[3, -6, 6], [10, 7, -9], [-3, -7, 9], [-8, 0, 4]])  # real input
# points = np.array([[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]])  # example 1
velocities = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(points)
originalPoints = np.copy(points)
originalVelocities = np.copy(velocities)


def calc_velocity(p, v):
    for point in range(len(p)):  # One point at a time
        for xyz in range(len(p[point])):  # Look at all dimensions
            for compare in range(len(p)):
                if p[point][xyz] > p[compare][xyz]:  # gravitate in positive direction
                    v[point][xyz] = v[point][xyz] - 1
                if p[point][xyz] < p[compare][xyz]:  # gravitate in negative direction
                    v[point][xyz] = v[point][xyz] + 1


def add_velocity(p, v):
    for i in range(len(p)):
        p[i] = np.add(p[i], v[i])


def calc_energy(p, v):
    result = 0
    for i in range(len(p)):
        potential_energy = abs(p[i][0]) + abs(p[i][1]) + abs(p[i][2])
        kinetic_energy = abs(v[i][0]) + abs(v[i][1]) + abs(v[i][2])
        result += potential_energy * kinetic_energy
    return result


time_steps = 0
x_match = 0
y_match = 0
z_match = 0

while not (x_match and y_match and z_match):
    calc_velocity(points, velocities)
    add_velocity(points, velocities)
    time_steps += 1
    if (not x_match) and (np.hsplit(points, 3)[0] == np.hsplit(originalPoints, 3)[0]).all() and \
     (np.hsplit(velocities, 3)[0] == np.hsplit(originalVelocities, 3)[0]).all():
        print("Match at x axis on iteration " + str(time_steps))
        x_match = time_steps
    if (not y_match) and (np.hsplit(points, 3)[1] == np.hsplit(originalPoints, 3)[1]).all() and \
     (np.hsplit(velocities, 3)[1] == np.hsplit(originalVelocities, 3)[1]).all():
        print("Match at y axis on iteration " + str(time_steps))
        y_match = time_steps
    if (not z_match) and (np.hsplit(points, 3)[2] == np.hsplit(originalPoints, 3)[2]).all() and \
     (np.hsplit(velocities, 3)[2] == np.hsplit(originalVelocities, 3)[2]).all():
        z_match = time_steps
        print("Match at z axis on iteration " + str(time_steps))

print("Ended up with " + str(calc_energy(points, velocities)) + " energy after " + str(time_steps) + " time steps.")
print("Least common multiple of each axis is: " + str([x_match, y_match, z_match]))
print("Universe will repeat after " + str(x_match * y_match * z_match) + " time steps, but sooner post-factoring?")
# 6849 is answer for part 1!
# Your puzzle answer was 356658899375688.

