from re import finditer, search

numberPattern = r"[0-9]+"
symbolPattern = r"[^.\n]+"

input = open("03_input.txt").readlines()
maxLines = len(input)
sum = 0


def clamp(nr, lower, upper):
    return max(lower, min(nr, upper))


def surroundingText(lineNr, span, lineLength):
    text = ""
    if lineNr > 0:
        text += input[lineNr - 1][
            clamp(span[0] - 1, 0, lineLength) : clamp(span[1] + 1, 0, lineLength)
        ]
    if span[0] > 0:
        text += input[lineNr][span[0] - 1]
    if span[1] < lineLength - 1:
        text += input[lineNr][span[1]]
    if lineNr < maxLines - 1:
        text += input[lineNr + 1][
            clamp(span[0] - 1, 0, lineLength) : clamp(span[1] + 1, 0, lineLength)
        ]
    return text


for lineNr in range(0, maxLines):
    line = input[lineNr]
    lineLength = len(line)
    numberMatches = finditer(numberPattern, line)
    for match in numberMatches:
        if search(symbolPattern, surroundingText(lineNr, match.span(), lineLength)):
            sum += int(match.group(0))

print(sum)

# INCORRECT ANSWERS:
#   554887 (too high)
