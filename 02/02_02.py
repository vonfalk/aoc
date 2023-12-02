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
	maxRed = 0
	maxGreen = 0
	maxBlue = 0
	for game in games:
		red = findall(redPattern, game)
		green = findall(greenPattern, game)
		blue = findall(bluePattern, game)
		if len(red) > 0:
			if maxRed < int(red[0]):
				maxRed = int(red[0])
		if len(green) > 0:
			if maxGreen < int(green[0]):
				maxGreen = int(green[0])
		if len(blue) > 0:
			if maxBlue < int(blue[0]):
				maxBlue = int(blue[0])
	sum += maxRed * maxGreen * maxBlue
print(sum)

# CORRECT ANSWER:
# 86036