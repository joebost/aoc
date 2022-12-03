from os import defpath


input = []

with open("input.txt") as f:
    for line in f.readlines():
        input.append(str(line).rstrip("\n"))

horizontal = depth = aim = 0
for i in input:
    direction, amount = i.split(" ")
    if direction == "forward":
        horizontal += int(amount)
        depth += aim * int(amount)
    elif direction == "down":
        aim += int(amount)
    else:
        aim -= int(amount)

print(horizontal * depth)