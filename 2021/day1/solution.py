input = []

with open("input.txt") as f:
    for line in f.readlines():
        input.append(int(line))

new_input = []
for i in range(2, len(input)):
    new_input.append(int(input[i] + input[i - 1] + input[i - 2]))

prev = None
res = 0
for x in new_input:
    if prev is not None and prev < int(x):
        res += 1
    prev = x

print(new_input)
print(res)
