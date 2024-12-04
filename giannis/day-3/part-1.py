import re

mult_regex = r"mul\(\d+,\d+\)"

with open("input.txt", "r") as file:
    lines = file.readlines()

sum = 0
for line in lines:
    results = re.findall(mult_regex, line)
    for multiplication in results:
        operand_regex = r"\d+,\d+"
        operand_results = re.findall(operand_regex, multiplication)
        operands = [int(operand) for operand in operand_results[0].split(",")]
        sum += operands[0] * operands[1]
print(sum)
