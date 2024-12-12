from re import findall

numberPattern = r"[0-9]+"
input = open("04_input.txt").readlines()


def getScore(score):
    if score == 0:
        return 0
    return pow(2, score - 1)


score = 0
for line in input:
    numbers = line.split(": ")[1].split(" | ")
    lhs = findall(numberPattern, numbers[0])
    rhs = findall(numberPattern, numbers[1])
    count = 0
    for nr in lhs:
        if nr in rhs:
            count += 1
    score += getScore(count)

print(score)
