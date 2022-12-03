input = []

with open("input.txt") as f:
    for line in f.readlines():
        input.append(str(line).rstrip("\n"))

min_needed = len(input) / 2
bin_num = ""
for i in range(len(input[0])):
    the_sum = sum(int(x[i]) for x in input)
    bin_num += "1" if the_sum >= min_needed else "0"

int_num = int(bin_num, 2)
inverse_s = "".join(["1" if i == "0" else "0" for i in bin_num])
inverse_int_num = int(inverse_s, 2)

print(int_num * inverse_int_num)
