import typing

with open("input1") as file:
    input = file.readlines()

list1 = []
list2 = []

for line in input:
    num1, num2 = line.split("   ")
    list1.append(num1)
    list2.append(num2)

list1.sort()
list2.sort()

res: list[int] = []

for n, i in enumerate(list1):
    # print(n, " ", i)
    res.append(abs(int(list1[n]) - int(list2[n])))

print(sum(res))

