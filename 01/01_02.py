from regex import findall

input = open("01_input.txt")
pattern = r"one|two|three|four|five|six|seven|eight|nine|[0-9]"
mapping = {
    "one": "1",
    "1": "1",
    "two": "2",
    "2": "2",
    "three": "3",
    "3": "3",
    "four": "4",
    "4": "4",
    "five": "5",
    "5": "5",
    "six": "6",
    "6": "6",
    "seven": "7",
    "7": "7",
    "eight": "8",
    "8": "8",
    "nine": "9",
    "9": "9",
}

sum = 0
for line in input:
    matches = findall(pattern, line, overlapped=True)
    sum += int(mapping.get(matches[0]) + mapping.get(matches[-1]))

print(sum)

# INCORRECT ANSWERS:
# 	50584 (too low)
