input = []

with open("input.txt") as f:
    for line in f.readlines():
        input.append(str(line).rstrip("\n"))
