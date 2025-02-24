from typing import List

# part 1
with open("input2") as file:
    input = file.read().splitlines()

# input: list of strings, one level each.

safe_num = 0;

def check_levels(levels: List[int]):
    increasing_base = True if levels[1] - levels[0] > 0 else False
    for i in range(len(levels)-1):
        diff = levels[i + 1] - levels[i]
        increasing = True if diff > 0 else False

        # checks
        if diff > 3 or diff < -3 or diff == 0: return False
        if increasing != increasing_base: return False
    return True

for level_string in input:
    levels_num = []
    for i in level_string.split(" "):
        levels_num.append(int(i))
    safe_num += check_levels(levels_num)
    
print("safe levels: ", safe_num)





