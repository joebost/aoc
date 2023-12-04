from utils.api import get_input

input_str = get_input(2)

# p1

"""
0 - lost
3 - draw
6 - win

1 - A/X rock
2 - B/Y paper
3- C/Z scissors
"""

ROCK = "A"
PAPER = "B"
SCISSORS = "C"

ROCK_1 = "X"
PAPER_2 = "Y"
SCISSORS_3 = "Z"


match_ups = {
    "A X": 4, # tie
    "A Y": 8, # win
    "A Z": 3, # loss
    "B X": 1, # loss
    "B Y": 5, # tie
    "B Z": 9, # win
    "C X": 7, # win
    "C Y": 2, # loss
    "C Z": 6, # tie
}

total = 0
match_up_strs = input_str.split("\n")

for match in match_up_strs:
    total += match_ups[match]

print(total)

# p2
"""
X = loss
Y = draw
Z = win
"""

new_match_ups = {
    "A X": 3, # scissors
    "A Y": 4, # rock
    "A Z": 8, # paper
    "B X": 1, # rock
    "B Y": 5, # paper
    "B Z": 9, # scissors
    "C X": 2, # paper
    "C Y": 6, # scissors
    "C Z": 7, # rock
}

total = 0
for match in match_up_strs:
    total += new_match_ups[match]

print(total)