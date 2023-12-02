from re import search

input = open("input.txt")
redPattern = r"[0-9]+(?= red)"
greenPattern = r"[0-9]+(?= green)"
bluePattern = r"[0-9]+(?= blue)"

maxColors = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

id = 0
sum = 0
for line in input:
    id += 1
    impossible = False
    games = line.split(": ")[1].split("; ")
    for game in games:
        red = search(redPattern, game)
        if red:
            if int(red[0]) > maxColors["red"]:
                impossible = True
                break

        green = search(greenPattern, game)
        if green:
            if int(green[0]) > maxColors["green"]:
                impossible = True
                break

        blue = search(bluePattern, game)
        if blue:
            if int(blue[0]) > maxColors["blue"]:
                impossible = True
                break
    if impossible:
        continue
    sum += id

print(sum)

# INCORRECT ANSWERS:
# 	4106 (too high)
