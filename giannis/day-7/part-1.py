sum = 0


# for every combination, create next set of combinations with a given operand
def gen_combinations(combinations: list[int], operand: int) -> list[int]:
    next = []
    for num in combinations:
        next.append(num + operand)
        next.append(num * operand)
    return next


def has_result(operands: list[int]):
    # initialise with just the first operand
    combinations = [operands[0]]

    # iterate over next operands
    for i in range(len(operands) - 1):
        # and store combinations of old combinations with next operand
        combinations = gen_combinations(combinations, operands[i + 1])

        # if a combination matches the result but there are more operands left it's not valid
        is_last_operand = i == len(operands) - 2
        if result in combinations and is_last_operand:
            return True

    return False


with open("input.txt", "r") as file:
    text = file.read().splitlines()

    for each in text:
        result = int(each.split(":")[0])
        operands = [int(num) for num in each.split(":")[1].strip().split(" ")]

        if has_result(operands):
            sum += result

print(sum)
