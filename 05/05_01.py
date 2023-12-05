from re import findall

input = open("05_input.txt").readlines()
numberPattern = "[0-9]+"

maps = [{}, {}, {}, {}, {}, {}, {}]
map_mode = -1


def get_final_dest(maps, index):
    dest = index
    for i in range(0, 7):
        for nr in maps[i]:
            if dest >= nr and dest <= nr + maps[i][nr][1]:
                dest = dest - nr + maps[i][nr][0]
                break
    return dest


for line in input[1:]:
    if line.find("map") > 0:
        map_mode += 1
        continue
    numberMatches = findall(numberPattern, line)
    if numberMatches:
        maps[map_mode][int(numberMatches[1])] = (
            int(numberMatches[0]),
            int(numberMatches[2]),
        )

seeds = findall(numberPattern, input[0])
lowest = int(seeds[0])
for i in seeds[1:]:
    dest = get_final_dest(maps, int(i))
    if dest < lowest:
        lowest = dest

print(lowest)
