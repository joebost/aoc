input = []

from statistics import median

with open("input.txt") as f:
    for line in f.readlines():
        for x in line.split(","):
            input.append(str(x).rstrip("\n"))

print(sum(int(x) for x in input) / len(input))

# 474
s = 0
for x in input:
    diff = abs(int(x) - 473)
    s += sum(range(1, diff + 1))

print(sum(range(0, 3)))
print(s)
print(median(int(x) for x in input))
