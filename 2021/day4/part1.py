input = []

with open("input.txt") as f:
    for line in f.readlines():
        input.append(str(line).rstrip("\n"))


"""
convert line 1 into a list for random numbers chosen
convert each board into a 2d array

for each move
check every row in the board for the number
if the number matches set it to 0 and do check win function on current position in the board
if win, select that board in exit

sum all numbers in board, multiply by the number that was called
"""

numbers_called = input[0].split(",")
boards = list(list(list()))

for x in range(1):
    boards.append(list())
    for i in range(2, 8):
      for i in range(5)
        boards[0].append(input[i].split(","))

print(boards)
