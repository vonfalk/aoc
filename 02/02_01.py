from re import findall

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
		red = findall(redPattern, game)
		green = findall(greenPattern, game)
		blue = findall(bluePattern, game)
		if len(red) > 0:
			if int(red[0]) > maxColors["red"]:
				impossible = True
				break
		if len(green) > 0:
			if int(green[0]) > maxColors["green"]:
				impossible = True
				break
		if len(blue) > 0:
			if int(blue[0]) > maxColors["blue"]:
				impossible = True
				break
	if impossible:
		continue
	sum += id
print(sum)

# INCORRECT ANSWERS:
# 	4106 (too high)

# CORRECT ANSWER:
# 2600