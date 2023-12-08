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
cur = [x for x in nnodes.keys() if x.endswith("A")]
res = [0] * len(cur)
while not verify(cur):
    for i in instructions:
        moves += 1
        for a, c in enumerate(cur):
            new = None
            if i == 'L':
                new = nnodes[c][0]
            else:
                new = nnodes[c][1]
            cur[a] = new
            # if new.endswith("Z") and res[a] == 0:
            #     print(f"found {a}")
            #     # res[a] = moves
        # if 0 not in res:
        #     print(res)
        #     exit()
        if verify(cur):
            print(moves)
            exit()

print(moves)
