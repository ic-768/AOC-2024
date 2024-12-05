# directions_to_check = [
#    # x, y
#    (1, 1),  # down and right
#    (-1, 1),  # down and left
#    (1, -1),  # up and right
#    (-1, -1),  # up and left
# ]


def check_neighbors(text, x, y):
    max_index = len(text) - 2

    # out of bounds
    if x < 1 or x > max_index or y < 1 or y > max_index:
        return False

    down_right = text[y + 1][x + 1]
    down_left = text[y - 1][x + 1]
    up_right = text[y + 1][x - 1]
    up_left = text[y - 1][x - 1]

    #  S S
    #   A
    #  M M
    if down_right == "M" and up_left == "S" and down_left == "M" and up_right == "S":
        return True
    # M M
    #  A
    # S S
    elif down_right == "S" and up_left == "M" and down_left == "S" and up_right == "M":
        return True

    # S M
    #  A
    # S M
    elif down_right == "M" and up_left == "S" and down_left == "S" and up_right == "M":
        return True

    #  M S
    #   A
    #  M S
    elif down_right == "S" and up_left == "M" and down_left == "M" and up_right == "S":
        return True

    return False


sum = 0
with open("input.txt", "r") as file:
    text = file.read().splitlines()
    for y, line in enumerate(text):
        for x, character in enumerate(line):
            if character == "A":
                if check_neighbors(text, x, y):
                    sum += 1

print(sum)
