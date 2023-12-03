from re import finditer

numberPattern = r"[0-9]+"
charPattern = r"[^.0-9]+"

input = open("03_input.txt").readlines()
maxLines = len(input)


def isPartNumber():
    pass


for i in range(0, maxLines):
    line = input[i]
    numberMatches = finditer(numberPattern, line)
    for match in numberMatches:
        print(match)
