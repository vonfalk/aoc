from re import search

data = open("data.txt")
pattern = "[0-9]"

sum = 0
for l in data:
	nr = int(search(pattern, l).group(0) + search(pattern, l[::-1]).group(0))
	sum += nr

print(sum)