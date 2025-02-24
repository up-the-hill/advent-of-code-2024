with open("input1") as file:
    input = file.read().splitlines()

# part 1
# time complexity: O(n)
# space complexity: O(n)
list1 = []
list2 = []

for line in input:
    num1, num2 = line.split("   ")
    list1.append(num1)
    list2.append(num2)

list1.sort()
list2.sort()

total_distance = []

for n, i in enumerate(list1):
    # print(n, " ", i)
    total_distance.append(abs(int(list1[n]) - int(list2[n])))

print("total distance: ", sum(total_distance))

# part 2
dict1 = dict()
dict2 = dict()
for i in range(len(input)):
    num1 = int(list1[i])
    num2 = int(list2[i])
    dict1[num1] = dict1.get(num1, 0) + 1
    dict2[num2] = dict2.get(num2, 0) + 1

similarity_score = 0
for i in dict1.keys():
    similarity_score += dict1[i] * dict2.get(i, 0)

for i in list1:
    print(i)

print(similarity_score)


