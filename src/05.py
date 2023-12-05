from utils.api import get_input
from dataclasses import dataclass

input_str = get_input(5)

@dataclass
class TranslationRange:
    lower: int
    upper: int
    offset: int # source - dest, translation = source - offset

m = {}
p2m = {}
keys = []
keys_type = "seed-to"
# p1
# parsing
def input_to_dataclasses(s: str):
    d = {}
    p2 = {}
    for line in s.split("\n"):
        dest, source, length = line.split()
        item = TranslationRange(lower=int(source), upper=int(source)+int(length), offset=int(source)-int(dest))
        p2_item = TranslationRange(lower=int(dest), upper=int(dest)+int(length), offset=int(dest)-int(source))
        d[source] = item
        p2[int(dest)]=p2_item
    return d, p2

for section in input_str.split("\n\n"):
    if "seeds: " in section: 
        keys = [int(x) for x in section.split(": ")[1].split()]
        continue 
    name, data = section.split(":\n")
    m[name], p2m[name] = input_to_dataclasses(data)

#p2 changes, just reuse p1 logic and stick all the seed ranges as single entries into our keys, slow af
# but should work
# keys = []
# seeds_str = input_str.split("\n\n")[0].split(": ")[1]
# seeds_list = seeds_str.split()
# for i in range(0, len(seeds_list), 2):
#     lower, r = int(seeds_list[i]), int(seeds_list[i+1])
#     for i in range(lower, lower+r):
#         keys.append(i)
# print(f"size of keys {len(keys)}")
# end p2 changes
# THIS WAS TOO SLOW

while keys_type != "location-to":
    map_name = [k for k in m if keys_type in k][0]
    current_map = m[map_name]
    print(f"working on {map_name}")

    new_keys = []
    for key in keys:
        new_key = key
        for tr in sorted(current_map):
            if key >= current_map[tr].lower and key < current_map[tr].upper:
                new_key = key-current_map[tr].offset
                break
        new_keys.append(new_key)
    keys = new_keys
    keys_type = f"{map_name.split('-to-')[1].split()[0]}-to" # next key name


print(min(keys))

# NEW P2 APPROACH
# what if we treat seeds as just another thing-to-thing map and then try every possible
# location and stop once we land in range of one of the seeds
# 1. add 

seeds_str = input_str.split("\n\n")[0].split(": ")[1]
seeds_list = seeds_str.split()
search_range = []
for i in range(0, len(seeds_list), 2):
    lower, r = int(seeds_list[i]), int(seeds_list[i+1])
    search_range.append((lower, r))

search_area = p2m["humidity-to-location map"]

def does_loc_end_in_seed_range(loc):
    key = loc
    key_type = "to-location"
    while key_type != "to-seed":
        map_name = [k for k in p2m if key_type in k][0]
        current_map = p2m[map_name]

        new_key = key
        for tr in sorted(current_map):
            if key >= current_map[tr].lower and key < current_map[tr].upper:
                new_key = key-current_map[tr].offset
                break
        key = new_key
        key_type = f"to-{map_name.split('-to-')[0]}"
    
    for sr in search_range:
        if key >= sr[0] and key < (sr[0]+sr[1]):
            return True
    return False


i = 1850000
while i < 1928061:
    # if i % 1000000 == 0: print(f"searching {i}")
    if does_loc_end_in_seed_range(i):
        print(i)
        exit()
    i += 1

    # for loc_range in sorted(search_area):
    #     print(f"searching {loc_range} -> {search_area[loc_range].upper}")
    #     for i in range(loc_range, search_area[loc_range].upper):
    #         if i % 100000 == 0: print(f"doing {i}")
    #         if does_loc_end_in_seed_range(i):
    #             print(i)
    #             exit()
    # break

"""
search_area - list of ranges in location (end state)
search_range - tuples of seed ranges (starting points)

"""
