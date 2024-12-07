sum = 0


def gen_combinations(x: list[int], y: int) -> list[int]:
    res = []
    for num in x:
        res.append(num + y)
        res.append(num * y)
    return res


def has_result(operands, results):
    for i in range(len(operands) - 1):
        results = gen_combinations(results, operands[i + 1])
        if result in results:
            return True
    return False


with open("input.txt", "r") as file:
    text = file.read().splitlines()

    for each in text:
        result = int(each.split(":")[0])
        operands = [int(num) for num in each.split(":")[1].strip().split(" ")]
        results = [operands[0]]

        if has_result(operands, results):
            sum += result

print(sum)
