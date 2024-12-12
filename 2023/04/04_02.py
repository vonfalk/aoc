from re import findall

input = open("04_input.txt").readlines()
maxLines = len(input)
numberPattern = r"[0-9]+"


def addOrSet(container, index, value):
    if container.get(index):
        container[index] += value
    else:
        container[index] = value


cards = {}
sum = 0
for lineNr in range(0, maxLines):
    count = 0
    numbers = input[lineNr].split(": ")[1].split(" | ")
    lhs = findall(numberPattern, numbers[0])
    rhs = findall(numberPattern, numbers[1])

    addOrSet(cards, lineNr, 1)
    sum += cards[lineNr]

    for nr in lhs:
        if nr in rhs:
            count += 1
            addOrSet(cards, lineNr + count, cards[lineNr])

print(sum)
