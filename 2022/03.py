from utils.api import get_input

input_str = get_input(3)

# p1
offset = ord('A')
s = input_str.split("\n")
pairs = []
total = 0

for s2 in s:
    firstpart, secondpart = s2[:len(s2)//2], s2[len(s2)//2:]

    occur = {}
    for c in firstpart:
        occur[c] = True

    for c in secondpart:
        if c in occur:
            print(f"{c} is in {firstpart} and {secondpart}")
            if ord(c) < ord('a'):
                value = ord(c) - ord('A') + 26 + 1
                total += value
            else:
                value = ord(c) - ord('a') + 1
                total += value
            break


print(total)
    
# p2
total = 0
for i in range(0, len(s), 3):
    one, two, three = s[i], s[i+1], s[i+2]
    m = {}

    for c in one:
        m[c] = [False]
    
    for c in two:
        if c in m:
            m[c] = [True]
    
    for c in three:
        if c in m and m[c] == [True]:
            if ord(c) < ord('a'):
                value = ord(c) - ord('A') + 26 + 1
                total += value
            else:
                value = ord(c) - ord('a') + 1
                total += value
            break

print(total)
    

