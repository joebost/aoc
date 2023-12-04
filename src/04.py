from utils.api import get_input
from typing import List
import collections

input_str = get_input(4)
cards = {}
    
res = 0
for i, card in enumerate(input_str.split("\n")):
    card_num = i+1
    winning, have = card.split(" | ")
    winning = winning.split(": ")[1]
    winning = [int(x) for x in winning.split()]
    have = [int(x) for x in have.split()]
    count = 0
    p2_count = 0
    for num in have:
        if num in winning:
            p2_count += 1
            count = 1 if count == 0 else count*2
    res += count
    cards[card_num] = [card_num+x for x in range(1, p2_count+1)]


print(res)


# p2
res2 = 0
q = collections.deque()
for c in cards.keys():
    res2 += 1
    q.append(c)

while q:
    cur = q.popleft()
    for x in cards[cur]:
        res2 +=1
        q.append(x)

print(res2)


