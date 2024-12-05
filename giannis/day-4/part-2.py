directions_to_check = [
    # x, y
    (1, 1),  # down and right
    (-1, 1),  # down and left
    (1, -1),  # up and right
    (-1, -1),  # up and left
]


def check_neighbors(text, x, y):
    # TODO replace magic numbers with len of lines
    two_char_buffer = len(text) - 2
    if x < 1 or x > two_char_buffer or y < 1 or y > two_char_buffer:
        # out of bounds
        return

    for dx, dy in directions_to_check:
        char = text[y + dy][x + dx]
        if char != "M" and char != "S":
            return False
    return True


sum = 0
with open("input.txt", "r") as file:
    text = file.read().splitlines()
    for y, line in enumerate(text):
        for x, character in enumerate(line):
            if character == "A":
                if check_neighbors(text, x, y):
                    sum += 1

print(sum)
