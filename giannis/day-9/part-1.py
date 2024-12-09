import re

with open("input.txt", "r") as file:
    text = file.read().splitlines()[0]
    char_number = 0

    decoded = []
    for x, char in enumerate(text):
        not_free = x % 2 == 0

        if not_free:
            # we don't use .extend because it would combine multi-digit numbers into one entry
            for i in range(int(char)):
                # append them as many times as needed
                decoded.append(str(char_number))
            char_number += 1

        else:
            decoded.extend("." * int(char))

for i in range(len(decoded) - 1, -1, -1):
    first_free = decoded.index(".")

    # done sorting
    if first_free > i:
        break

    # swap number for free space
    if re.match(r"\d", decoded[i]):
        decoded[first_free] = decoded[i]
        decoded[i] = "."


sum = 0
filtered = [x for x in decoded if x != "."]


for i, each in enumerate(filtered):
    sum += int(each) * i

print("sum is", sum)
