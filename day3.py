import re

with open("input3") as file:
    input = file.read()

# PART 1
matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input)

sum = 0
for match in matches:
    sum += int(match[0]) * int(match[1])

print(sum)



