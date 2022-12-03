from utils.api import get_input

input_str = get_input(1)

# p1
s = input_str.split("\n")
elf_to_cal = [0]
for line in s:
    if line == "": 
        elf_to_cal.append(0)
    else:
        elf_to_cal[-1] += int(line)

print(max(elf_to_cal))

# p2
sort = sorted(elf_to_cal)
top_3_elves = sum(sort[-3:])
print(top_3_elves)
        