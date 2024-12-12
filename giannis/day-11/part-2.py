num_blinks = 0

with open("input.txt") as file:
    stones = [int(num) for num in file.read().split()]

    stone_counts = {}
    for stone in stones:
        if stone in stone_counts:
            stone_counts[stone] += 1
        else:
            stone_counts[stone] = 1

    while num_blinks < 75:
        next_counts = {}
        for stone in stone_counts:
            string = str(stone)
            num_stones = stone_counts[stone]

            # add number of pre-transformed stones to the transformed for the next-round
            if stone == 0:
                if 1 in next_counts:
                    next_counts[1] += num_stones
                else:
                    next_counts[1] = num_stones

            elif len(string) % 2 == 0:
                new_stones = list(
                    map(int, [string[: len(string) // 2], string[len(string) // 2 :]])
                )

                left = new_stones[0]
                right = new_stones[1]

                if (left) in next_counts:
                    next_counts[left] += num_stones
                else:
                    next_counts[left] = num_stones

                if (right) in next_counts:
                    next_counts[right] += num_stones
                else:
                    next_counts[right] = num_stones
            else:
                multiplied = stone * 2024

                if (multiplied) in next_counts:
                    next_counts[multiplied] += num_stones
                else:
                    next_counts[multiplied] = num_stones

        stone_counts = next_counts
        next_counts = {}
        num_blinks += 1
        print(stone_counts)

sum = 0
for stone in stone_counts:
    sum += stone_counts[stone]

print(sum)
