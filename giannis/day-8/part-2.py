import re

antenna_pattern = r"[a-zA-Z0-9]"


def is_antenna(char):
    return bool(re.match(antenna_pattern, char))


def get_distance(x1, y1, x2, y2):
    return {"x": x2 - x1, "y": y2 - y1}


antinodes = {}


with open("input.txt", "r") as file:
    text = [list(line) for line in file.read().splitlines()]

    for y, line in enumerate(text):
        for x, char_init in enumerate(line):
            if is_antenna(char_init):
                for y_seeked in range(y, len(text)):
                    # if on same line, start after current character, else start from beginning of line
                    start_index = x + 1 if y_seeked == y else 0

                    for x_seeked in range(start_index, len(line)):
                        if text[y_seeked][x_seeked] == char_init:
                            distance = get_distance(x, y, x_seeked, y_seeked)

                            # start at antennas
                            target_1 = {"y": y, "x": x}
                            target_2 = {
                                "y": y_seeked,
                                "x": x_seeked,
                            }

                            # iterate over both directions at fixed distance, adding antinodes
                            while 0 <= target_1["y"] < len(text) and 0 <= target_1[
                                "x"
                            ] < len(text):
                                # antennas count as antinodes too, so we set before incrementing
                                antinodes[
                                    target_1["y"],
                                    target_1["x"],
                                ] = "#"

                                target_1["y"] -= distance["y"]
                                target_1["x"] -= distance["x"]

                            while 0 <= target_2["y"] < len(text) and 0 <= target_2[
                                "x"
                            ] < len(line):
                                antinodes[
                                    target_2["y"],
                                    target_2["x"],
                                ] = "#"

                                target_2["y"] += distance["y"]
                                target_2["x"] += distance["x"]

for each in antinodes:
    y = each[0]
    x = each[1]
    text[y][x] = "#"

print(len(antinodes))
