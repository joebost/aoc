from utils.api import get_input

input_str = get_input(8)

# parsing
instructions = [c for c in input_str.split("\n")[0]]
nodes = input_str.split("\n")[2:]
adj = [x.split(" = ")[1].replace('(', '').replace(')', '') for x in nodes]
adj = [x.split(", ") for x in adj]
nodes = [x.split(" = ")[0] for x in nodes]
nnodes = {}
for i, node in enumerate(nodes):
    nnodes[node] = adj[i]

moves = 0
cur = "AAA"
# while cur != "ZZZ":
#     for i in instructions:
#         new = None
#         if i == 'L':
#             new = nnodes[cur][0]
#         else:
#             new = nnodes[cur][1]
#         moves += 1
#         cur = new
#         if cur == "ZZZ":
#             print(moves)
#             exit()

# print(moves)

# p2
"""
get all that start with A
then while all don't end with Z
for each instruction
for each cur, do move
verify
"""
def verify(x):
    l = len(x)
    n = len([a for a in x if a.endswith("Z")])
    if n > 3: print(x)

    return l == n 

assert verify(['AAZ', 'BBZ', 'CCZ', 'DDZ', 'ZZZ', 'XYZ']) == True

# 0 - loops every 20093
# 1 - loops every 12169
# 2 - loops every 13301
cur = [x for x in nnodes.keys() if x.endswith("A")]
res = [0] * len(cur)
import math
while True:
    for i in instructions:
        if i == 'L':
            cur = [nnodes[c][0] for c in cur]
        else:
            cur = [nnodes[c][1] for c in cur]
        moves += 1
        for j, c in enumerate(cur):
            if c.endswith('Z') and res[j] == 0:
                res[j] = moves
        
        if 0 not in res:
            print(math.lcm(*res))
            exit()
