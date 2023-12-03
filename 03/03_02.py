from re import finditer

numberPattern = r"[0-9]+"
symbolPattern = r"\*"

input = open("03_input.txt").readlines()
maxLines = len(input)
sum = 0


def clamp(nr, lower, upper):
    return max(lower, min(nr, upper))


def countNumbers():
    pass


for lineNr in range(0, maxLines):
    line = input[lineNr]
    lineLength = len(line)
    symbolMatches = finditer(symbolPattern, line)
    for match in symbolMatches:
        pass
