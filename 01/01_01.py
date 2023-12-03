from regex import findall

input = open("01_input.txt")
pattern = "[0-9]"

sum = 0
for line in input:
    matches = findall(pattern, line)
    sum += int(matches[0] + matches[-1])

print(sum)
