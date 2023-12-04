from utils.api import get_input
import math

input_str = get_input(3)

# p1
sl = set() # tuples of all locations that aren't numbers or .
for i, row in enumerate(input_str.split("\n")):
    for j, c in enumerate(row):
        if not c.isdigit() and c != ".":
            sl.add((i, j))

def is_part(i, j):
    for ii in range(-1, 2):
        for jj in range(-1, 2):
            if (i+ii, j+jj) in sl:
                return True
    return False

res = 0
for i, row in enumerate(input_str.split("\n")):
    visited = set()
    for j, c in enumerate(row):
        if c.isdigit() and j not in visited:
            begin = j
            while j < len(row) and row[j].isdigit():
                visited.add(j)
                j += 1
            num = int(row[begin:j])
            for x in range(begin, j):
                if is_part(i, x):
                    print(f"{num} is a part")
                    res += num
                    break

nums = {}
gears = set()

key = 0
for i, row in enumerate(input_str.split("\n")):
    visited = set()
    for j, c in enumerate(row):
        if c == "*":
            gears.add((i, j))

        if c.isdigit() and j not in visited:
            cords = set()
            begin = j
            while j < len(row) and row[j].isdigit():
                visited.add(j)
                cords.add((i, j))
                j += 1
            num = int(row[begin:j])
            for cord in cords:
                nums[cord] = (num, key)
            key += 1

res = 0
for gear in gears:
    keys = set()
    adj = set()
    i,j = gear
    for ii in range(-1, 2):
        for jj in range(-1, 2):
            if (i+ii, j+jj) in nums and nums[i+ii, j+jj][1] not in keys:
                adj.add(nums[i+ii, j+jj][0])
                keys.add(nums[i+ii, j+jj][1])
    if len(adj) == 2:
        res += math.prod(x for x in adj)

print(res)



