import re

sum = 0

with open("input.txt", "r") as file:
    (rule_section, page_section) = file.read().split("\n\n")

    rules = rule_section.split("\n")
    rules = [re.findall(r"(\d+)", item) for item in rules]
    rules = [[int(num) for num in pair] for pair in rules]

    page_lines = page_section.split("\n")
    page_lines = [item.split(",") for item in page_lines]
    page_lines.pop()
    page_lines = [[int(num) for num in item] for item in page_lines]

    for line in page_lines:
        for index, rule in enumerate(rules):
            # rule applies
            if rule[0] in line and rule[1] in line:
                # rule is broken
                if line.index(rule[1]) < line.index(rule[0]):
                    break

            # passed all rules successfully
            is_last_rule = index == len(rules) - 1
            if is_last_rule:
                middle_element = line[len(line) // 2]
                sum += middle_element

print(sum)
