import re

sum = 0

with open("input.txt", "r") as file:
    (r, p) = file.read().split("\n\n")

    rules = r.split("\n")
    page_lines = p.split("\n")
    page_lines = [item.split(",") for item in page_lines]
    page_lines.pop()
    page_lines = [[int(num) for num in item] for item in page_lines]

    rules = [re.findall(r"(\d+)", item) for item in rules]
    rules = [[int(num) for num in pair] for pair in rules]

    for line in page_lines:
        for index, rule in enumerate(rules):
            if rule[0] in line and rule[1] in line:
                if line.index(rule[1]) < line.index(rule[0]):
                    break

            if index == len(rules) - 1:
                sum += line[len(line) // 2]

print(sum)
