from utils.api import get_input
import re

input_str = get_input(1).split('\n')

def p1():
    res = 0
    for line in input_str:
        rev = line[::-1]
        first = re.search(r"\d", line)
        last = re.search(r"\d", rev)
        num = int(f"{line[first.start()]}{rev[last.start()]}")
        res += num

    print(res)

p1()

# P2
def p2():
    def first_digit(line, rev=False):
        words = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
        first = re.search(r"\d", line).start()
        digit = int(line[first])
        for word in words.keys():
            i = line.find(word)
            if rev:
                i = line.find(word[::-1])
            if i < first and i != -1:
                first, digit = i, words[word]
        
        return digit

    res = 0
    for line in input_str:
        res += int(f"{first_digit(line)}{first_digit(line[::-1], True)}")
    
    print(res)

p2()