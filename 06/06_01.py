from math import ceil, floor, sqrt
from re import findall

input = open("06_input.txt").readlines()
number_pattern = "[0-9]+"

times = findall(number_pattern, input[0])
dists = findall(number_pattern, input[1])

wins = 1
for gameNr in range(0, len(times)):
    t = int(times[gameNr])
    d = int(dists[gameNr])
    min = t / 2 - sqrt((t / 2) ** 2 - d)
    max = t / 2 + sqrt((t / 2) ** 2 - d)

    if min % 1.0 == 0:
        min = int(min + 1)
    else:
        min = ceil(min)
    if max % 1.0 == 0:
        max = int(max - 1)
    else:
        max = floor(max)
    wins *= max - min + 1

print(wins)
