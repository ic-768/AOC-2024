import re

# matches mult(x,y) operation
mult_pattern = r"mul\(\d+,\d+\)"
# matches the numbers
operand_pattern = r"\d+,\d+"
# matches don't block
dont_pattern = r"(?<=don't).*?(?=\bdon't\b|do)"


with open("input.txt", "r") as file:
    text = file.read()
    # clean don't blocks
    cleaned_text = re.sub(dont_pattern, "", text, flags=re.DOTALL)

    # same as part 1
    sum = 0
    results = re.findall(mult_pattern, cleaned_text)
    for multiplication in results:
        operand_results = re.findall(operand_pattern, multiplication)
        operands = [int(operand) for operand in operand_results[0].split(",")]
        sum += operands[0] * operands[1]
    print(sum)
