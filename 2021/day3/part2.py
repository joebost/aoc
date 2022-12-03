from statistics import mode

input = []

with open("input.txt") as f:
    for line in f.readlines():
        input.append(str(line).rstrip("\n"))

temp = input.copy()
index = 0

# while list is not one element
# find most common occuring digit at index i
# eleminate all elements that don't have the most common digit
# repeat on new subset of list

while len(temp) > 1:
    subset = temp.copy()

    # find most common
    num_ones = num_zeros = 0
    least_common = "1"
    for x in subset:
        if x[index] == "0":
            num_zeros += 1
        else:
            num_ones += 1

    if num_ones >= num_zeros:
        least_common = "0"

    # remove least common
    temp = list(filter(lambda x: x[index] == least_common, subset))
    index += 1
    print(temp)

print(f"{temp[0]}")
print(int(temp[0], 2))

# 1427, 1426
print(1427 * 2502)
