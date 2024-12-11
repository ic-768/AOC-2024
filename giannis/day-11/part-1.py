num_blinks = 0

with open("input.txt") as file:
    stones = [int(num) for num in file.read().split()]

    while num_blinks < 25:
        output = []
        for stone in stones:
            string = str(stone)
            if stone == 0:
                output.append(1)
            elif len(string) % 2 == 0:
                new_stones = [string[: len(string) // 2], string[len(string) // 2 :]]
                output.extend(list(map(int, new_stones)))
            else:
                output.append(stone * 2024)

        stones = output
        num_blinks += 1
        print(len(output))
