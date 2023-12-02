from re import search

input = open("input.txt")
redPattern = r"[0-9]+(?= red)"
greenPattern = r"[0-9]+(?= green)"
bluePattern = r"[0-9]+(?= blue)"

id = 0
sum = 0
for line in input:
	id += 1
	games = line.split(": ")[1].split("; ")
	maxRed = maxGreen = maxBlue = 0
	for game in games:
		red = search(redPattern, game)
		if red:
			if maxRed < int(red[0]):
				maxRed = int(red[0])

		green = search(greenPattern, game)
		if green:
			if maxGreen < int(green[0]):
				maxGreen = int(green[0])

		blue = search(bluePattern, game)
		if blue:
			if maxBlue < int(blue[0]):
				maxBlue = int(blue[0])
	sum += maxRed * maxGreen * maxBlue

print(sum)
