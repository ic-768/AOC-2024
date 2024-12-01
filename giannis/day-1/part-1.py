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

sum = 0

for i in range(len(sorted1)):
    left_element = sorted1[i]
    right_element = sorted2[i]
    sum += abs(left_element - right_element)

print(sum)
