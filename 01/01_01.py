from regex import findall

input = open("01_input.txt")
pattern = "[0-9]"

sum = 0
for line in input:
    nr = int(findall(pattern, line)[0] + findall(pattern, line)[-1])
    sum += nr

print(sum)
