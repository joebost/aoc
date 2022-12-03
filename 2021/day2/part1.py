from os import defpath


input = []

with open("input.txt") as f:
    for line in f.readlines():
        input.append(str(line).rstrip("\n"))

horizontal = depth = 0
for i in input:
    direction, amount = i.split(" ")
    if direction == "forward":
        horizontal += int(amount)
    elif direction == "down":
        depth += int(amount)
    else:
        depth -= int(amount)

print(horizontal * depth)
