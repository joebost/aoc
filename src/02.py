from utils.api import get_input
import math

input_str = get_input(2)
#p1
res = 0
maxes = {"red": 12, "green":13, "blue":14}

def is_game_possible(s):
    indexes = {"red":s.find("red"), "blue":s.find("blue"), "green":s.find("green")}
    for color_name in indexes:
        color = indexes[color_name]
        if color != -1:
            num_of_cubes_index = color-2
            num = []
            while s[num_of_cubes_index].isdigit():
                num.insert(0, s[num_of_cubes_index])
                num_of_cubes_index-=1
            num = int("".join(str(x) for x in num))
            if num > maxes[color_name]:
                return False 
    return True

for i, game in enumerate(input_str.split("\n")):
    game_num = i+1
    res += game_num

    s = game.split(":")[1].strip()
    combos = s.split(";")

    for combo in combos:
        combo = combo.strip()
        if not is_game_possible(combo):
            res -= game_num
            break

print(res)

# p2
"""
for each game
find max of every color, default is 0 if color not found
mulitple and add to res
"""
def max_for_color(color, s):
    max_ = 0
    lines = s.replace(";", ",").split(",")
    for line in lines:
        if color in line:
            print(line)
            max_ = max(max_, [int(x) for x in line.split() if x.isdigit()][0])
    return max_

res = 0
for i, game in enumerate(input_str.split("\n")):
    s = game.split(":")[1].strip()
    res += math.prod([max_for_color(c,s) for c in ["red", "blue", "green"]])

print(res)