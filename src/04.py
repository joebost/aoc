from utils.api import get_input

input_str = get_input(4)

# p1
s = input_str.split("\n")
total = 0

def fully_contains(section, other):
  print(f"{section} contains {other}?")
  section_lower, section_upper = section.split("-")
  other_lower, other_upper = other.split("-")

  within_lower = int(section_lower) <= int(other_lower)
  within_upper = int(section_upper) >= int(other_upper)
  result = within_lower and within_upper
  if result: print(f"{section} does contain {other}")
  return result


for pair in s:
  one, two = pair.split(",")
  if fully_contains(one, two) or fully_contains(two, one): total += 1

print(total)

# p2

def contains(section, other):
  print(f"{section} contains {other}?")
  section_lower, section_upper = section.split("-")
  other_lower, other_upper = other.split("-")

  lower = int(other_lower) >= int(section_lower) and int(other_lower) <= int(section_upper)
  upper = int(other_upper) >= int(section_lower) and int(other_upper) <= int(section_upper)
  return lower or upper

total = 0
for pair in s:
  one, two = pair.split(",")
  if contains(one, two) or contains(two, one): total += 1

print(total)


