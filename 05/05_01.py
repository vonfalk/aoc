from re import findall

input = open("05_input.txt").readlines()
numberPattern = "[0-9]+"

maps = [{}, {}, {}, {}, {}, {}, {}]
map_mode = -1
seeds = findall(numberPattern, input[0])


def get_dest(mapping, index):
    for nr in mapping:
        if index >= nr and index <= nr + mapping[nr][1]:
            return index - nr + mapping[nr][0]
    return index


def get_final_dest(maps, index):
    dest = index
    for i in range(0, 7):
        dest = get_dest(maps[i], dest)
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

lowest = int(seeds[0])
for i in seeds[1:]:
    dest = get_final_dest(maps, int(i))
    if dest < lowest:
        lowest = dest

print(lowest)
