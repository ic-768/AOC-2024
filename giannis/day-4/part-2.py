sum = 0

with open("input.txt", "r") as file:

    def has_xmas(x, y):
        max_index = len(text) - 2

        # out of bounds
        if x < 1 or x > max_index or y < 1 or y > max_index:
            return False

        down_right = text[y + 1][x + 1]
        down_left = text[y - 1][x + 1]
        up_right = text[y + 1][x - 1]
        up_left = text[y - 1][x - 1]

        diag_1 = f"{down_left}{up_right}"
        diag_2 = f"{down_right}{up_left}"

        return diag_1 in ["MS", "SM"] and diag_2 in ["MS", "SM"]

    text = file.read().splitlines()
    for y, line in enumerate(text):
        for x, character in enumerate(line):
            if character == "A":
                if has_xmas(x, y):
                    sum += 1

print(sum)
