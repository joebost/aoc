from utils.api import get_input
import math
input_str = get_input(6)

times, distances = input_str.split("\n")
times = times.split()[1:]
# times = [int(t) for t in times]
times = [int("".join(times))] # p2 change
distances = distances.split()[1:]
# distances = [int(d) for d in distances]
distances = [int("".join(distances))] # p2 change
print(times, distances)

res = []
for i, race_time in enumerate(times):
    loc_res = 0
    for hold_button_time in range(race_time+1):
        speed = hold_button_time
        time_left = race_time - hold_button_time
        distance = speed * time_left
        if distance >= distances[i]:
            loc_res+=1
    res.append(loc_res)

print(math.prod(res))

