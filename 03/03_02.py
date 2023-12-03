from re import finditer

numberPattern = r"[0-9]+"
symbolPattern = r"\*"

input = open("03_input.txt").readlines()
maxLines = len(input)
sum = 0


def isSurrounding(pos, span):
    return (span[0] - 1 <= pos and span[0] + 1 >= pos) or (
        span[1] - 1 <= pos and span[1] >= pos
    )


def getNearbyMatches(pos, line):
    matches = []
    for match in finditer(numberPattern, line):
        if isSurrounding(pos, match.span()):
            matches.append(int(match.group(0)))
    return matches


def calculateGearRatio(lineNr, pos):
    matches = []
    if lineNr > 0:
        matches += getNearbyMatches(pos, input[lineNr - 1])
    matches += getNearbyMatches(pos, input[lineNr])
    if lineNr < maxLines - 1:
        matches += getNearbyMatches(pos, input[lineNr + 1])
    if len(matches) == 2:
        return matches[0] * matches[1]
    return 0


for lineNr in range(0, maxLines):
    symbolMatches = finditer(symbolPattern, input[lineNr])
    for match in symbolMatches:
        sum += calculateGearRatio(lineNr, match.span()[0])

print(sum)

# INCORRECT ANSWERS:
# 	467835 (too low)
