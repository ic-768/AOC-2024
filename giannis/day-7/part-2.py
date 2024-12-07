# ! 227655036461766

sum = 0


with open("input.txt", "r") as file:
    text = file.read().splitlines()

    for each in text:
        result = int(each.split(":")[0])
        operands = [int(num) for num in each.split(":")[1].strip().split(" ")]
        combinations = [operands[0]]

        # iterate over every operand
        for i in range(len(operands) - 1):
            # get next operand
            operand = operands[i + 1]

            # accumulate combinations
            next_combinations = []

            # generate combinations
            for num in combinations:
                next_combinations.append(num + operand)
                next_combinations.append(num * operand)
                next_combinations.append(int(str(num) + str(operand)))

            # update combinations
            combinations = next_combinations

            if result in combinations:
                sum += result
                break

print(sum)
