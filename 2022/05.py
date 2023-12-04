from utils.api import get_input
import string
import copy

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
    n[int(c)] = m[i][::-1]

n2 = copy.deepcopy(n)
    
for move in moves.split("\n"):
  words = move.split(" ")
  amount, fromm, to = int(words[1]), int(words[3]), int(words[5])

  for i in range(amount):
    n[to].append(n[fromm].pop())

for num, stack in n.items():
  print(stack[-1], end="")

print()

n = n2

# p2
for move in moves.split("\n"):
  words = move.split(" ")
  amount, fromm, to = int(words[1]), int(words[3]), int(words[5])

  to_move = []
  for i in range(amount):
    to_move.insert(0, n[fromm].pop())
  
  n[to] += to_move

for num, stack in n.items():
  print(stack[-1], end="")

print()