from utils.api import get_input

input_str = get_input(9)

histories = [x.split() for x in input_str.split("\n")]
for i in range(len(histories)):
    histories[i] = [int(x) for x in histories[i]]
predicted_values = []
for h in histories:
    h.reverse() # one line change for part 2 🤣
    working = [h]
    while set(working[-1]) != set([0]):
        new = []
        for i in range(0, len(working[-1])-1):
            new.append(working[-1][i+1]-working[-1][i])
        working.append(new)
    
    predicted_value = 0
    for row in working[::-1]:
        predicted_value += row[-1]
    predicted_values.append(predicted_value)

print(sum(predicted_values))


