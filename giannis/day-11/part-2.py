num_blinks = 0

with open("sample.txt") as file:
    stones = [int(num) for num in file.read().split()]

    stone_counts = {}
    for stone in stones:
        if stone in stone_counts:
            stone_counts[stone] += 1
        else:
            stone_counts[stone] = 1

    while num_blinks < 6:
        next_counts = {}
        for stone in stone_counts:
            string = str(stone)

            # if transformed stone doesn't exist in next_counts, add num of pre-transformed
            # else increment by 1
            if stone == 0:
                if 1 in next_counts:
                    next_counts[1] += 1
                else:
                    next_counts[1] = stone_counts[stone]

            elif len(string) % 2 == 0:
                new_stones = list(
                    map(int, [string[: len(string) // 2], string[len(string) // 2 :]])
                )

                if (new_stones[0]) in next_counts:
                    next_counts[(new_stones[0])] += 1
                else:
                    next_counts[(new_stones[0])] = stone_counts[stone]

                if (new_stones[1]) in next_counts:
                    next_counts[(new_stones[1])] += 1
                else:
                    next_counts[(new_stones[1])] = stone_counts[stone]
            else:
                if (stone * 2024) in next_counts:
                    next_counts[stone] += 1
                else:
                    next_counts[stone * 2024] = stone_counts[stone]

        print(stone_counts)
        print("replaced by")
        print(next_counts)
        stone_counts = next_counts
        next_counts = {}
        num_blinks += 1

sum = 0
for stone in stone_counts:
    sum += stone_counts[stone]

print(sum)
