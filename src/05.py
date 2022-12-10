from utils.api import get_input
import string

input_str = get_input(5)

# WRITE YOUR SOLUTION HERE

crates, moves = input_str.split("\n\n")
lines = crates.split("\n")

print(crates)

m = {}
for line in lines:
  for i in range(len(line)):
    c = line[i]
    if c in string.ascii_uppercase:
      if i in m:
        m[i].append(c)
      else:
        m[i] = [c]

n = {}
for i in range(len(lines[-1])):
  c = lines[-1][i]
  if c != " ":
    n[c] = m[i]
    

print(n)
#todo

