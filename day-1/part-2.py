list1 = []
list2 = []

with open("input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    for index, number in enumerate(line.split()):
        if index % 2:
            list2.append(int(number))
        else:
            list1.append(int(number))

sorted1 = sorted(list1)
sorted2 = sorted(list2)

similarity = 0

for i in range(len(sorted1)):
    left_element = sorted1[i]
    occurrences = sorted2.count(left_element)
    similarity += left_element * occurrences

print(similarity)
