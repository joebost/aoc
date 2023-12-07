from utils.api import get_input
import collections

input_str = get_input(7)

card_strengths = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
hands = [x for x in input_str.split("\n")]
hands = [(x.split()[0], x.split()[1]) for x in hands]

# 5oak = 1, 4oak = 2, fh = 3, 3oak = 4, tp = 5, op = 6, hc = 7
def hand_type(hand):
    if(len(set(hand)) == 1): return 1
    if(sorted(list(collections.Counter(hand).values())) == [1, 4]): return 2 # 1J: 2 -> 1 4J: 2 -> 1
    if(sorted(list(collections.Counter(hand).values())) == [2, 3]): return 3 # 2J: 3 -> 1 3J: 3 -> 1
    if(sorted(list(collections.Counter(hand).values())) == [1, 1, 3]): return 4 # 1J: 4 -> 2 3J: 4 -> 2
    if(sorted(list(collections.Counter(hand).values())) == [1, 2, 2]): return 5 # 1J: 5 -> 3 2J: 5 -> 2
    if(sorted(list(collections.Counter(hand).values())) == [1, 1, 1, 2]): return 6 # 1J: 6 -> 4 2J: 6 -> 4
    if(sorted(list(collections.Counter(hand).values())) == [1, 1, 1, 1, 1]): return 7 # 1J: 7 -> 6 
    raise Exception(f"could not find hand type for {hand}")

def rescore_with_jokers(hand, old_score):
    num_jokers = collections.Counter(hand)['J']
    if old_score == 1: return 1
    if old_score == 2:
        if num_jokers > 0:
            return 1
    if old_score == 3:
        if num_jokers >= 2:
            return 1
    if old_score == 4:
        if num_jokers >= 1:
            return 2
    if old_score == 5:
        if num_jokers == 1:
            return 3
        if num_jokers == 2:
            return 2
    if old_score == 6:
        if num_jokers >= 1:
            return 4
    if old_score == 7:
        if num_jokers == 1:
            return 6
    return old_score

# 2J: 7 -> 4, 3J: 7 -> 2, 4J -> 1
assert hand_type("AAAAA") == 1
assert hand_type("AAAA9") == 2
assert hand_type("AAA99") == 3
assert hand_type("AAA98") == 4
assert hand_type("AA998") == 5
assert hand_type("AA987") == 6
assert hand_type("A6987") == 7

hands_grouped_by_type = collections.defaultdict(list)

for hand in hands:
    hands_grouped_by_type[rescore_with_jokers(hand[0], hand_type(hand[0]))].append(hand)

def custom_sort(hand):
    res = ""
    for c in hand:
        ord_value = chr(ord('a')+card_strengths.index(c))
        res += ord_value
    return res

for group in hands_grouped_by_type:
    hands_grouped_by_type[group].sort(key=lambda x: custom_sort(x[0]))

all_hands_sorted = []
for hand_type in sorted(hands_grouped_by_type.keys()):
    hand_group = hands_grouped_by_type[hand_type]
    all_hands_sorted += hand_group

all_hands_sorted.reverse()
print(all_hands_sorted)
res = 0
for multiplier, hand in enumerate(all_hands_sorted):
    _, bid = hand
    res += (multiplier+1)*int(bid)
print(res)





