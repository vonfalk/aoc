from math import ceil, floor, sqrt
from re import findall

input = open("06_input.txt").readlines()
number_pattern = "[0-9]+"


def solve_v(t, d):
    return [t / 2 - sqrt((t / 2) ** 2 - d), t / 2 + sqrt((t / 2) ** 2 - d)]


times = findall(number_pattern, input[0])
dists = findall(number_pattern, input[1])

wins = 1
for gameNr in range(0, len(times)):
    t = int(times[gameNr])
    d = int(dists[gameNr])
    v = solve_v(t, d)

    if v[0] % 1.0 == 0:
        v[0] = int(v[0] + 1)
    else:
        v[0] = ceil(v[0])
    if v[1] % 1.0 == 0:
        v[1] = int(v[1] - 1)
    else:
        v[1] = floor(v[1])
    wins *= v[1] - v[0] + 1

print(wins)
