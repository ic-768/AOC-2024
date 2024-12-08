import re

sum = 0
antenna_pattern = r"[a-zA-Z0-9]"


def is_antenna(char):
    return bool(re.match(antenna_pattern, char))


def get_distance(x1, y1, x2, y2):
    return [x2 - x1, y2 - y1]


antinodes = {}


with open("input.txt", "r") as file:
    text = [list(line) for line in file.read().splitlines()]

    for y, line in enumerate(text):
        for x, char_init in enumerate(line):
            if is_antenna(char_init):
                for y_seeked in range(y, len(text)):
                    for x_seeked in range(x + 1 if y_seeked == y else 0, len(line)):
                        if text[y_seeked][x_seeked] == char_init:
                            distance = get_distance(x, y, x_seeked, y_seeked)

                            # create symmetrical antinodes
                            if 0 <= y - distance[1] < len(text) and 0 <= x - distance[
                                0
                            ] < len(text):
                                antinodes[(y - distance[1], x - distance[0])] = "#"

                            if 0 <= y_seeked + distance[1] < len(
                                text
                            ) and 0 <= x_seeked + distance[0] < len(line):
                                antinodes[
                                    (y_seeked + distance[1], x_seeked + distance[0])
                                ] = "#"

    print(antinodes)
    for each in antinodes:
        y = each[0]
        x = each[1]
        text[y][x] = "#"

    result = "\n".join("".join(line) for line in text)

    print(result)
    print(len(antinodes))
