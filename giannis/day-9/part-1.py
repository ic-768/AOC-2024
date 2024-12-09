import re

with open("input.txt", "r") as file:
    text = file.read().splitlines()[0]
    char_number = 0

    decoded = []
    print("before first for loop")
    for x, char in enumerate(text):
        not_free = x % 2 == 0

        if not_free:
            decoded.extend(str(char_number) * int(char))
            char_number += 1

        else:
            decoded.extend("." * int(char))


print("before second for loop")
for i in range(len(decoded) - 1, -1, -1):
    first_free = decoded.index(".")
    if first_free > i:
        break

    if re.match(r"\d", decoded[i]):
        decoded[first_free] = decoded[i]
        decoded[i] = "."


sum = 0
filtered = [x for x in decoded if x != "."]

for x, char in enumerate(filtered):
    sum += int(char) * x

print(sum)
