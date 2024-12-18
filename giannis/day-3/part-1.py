import re

# matches mult(x,y) operation
mult_pattern = r"mul\(\d+,\d+\)"
# matches the numbers
operand_pattern = r"\d+,\d+"

with open("input.txt", "r") as file:
    text = file.read()

    sum = 0
    results = re.findall(mult_pattern, text)
    for multiplication in results:
        operand_results = re.findall(operand_pattern, multiplication)
        operands = [int(operand) for operand in operand_results[0].split(",")]
        sum += operands[0] * operands[1]
print(sum)
