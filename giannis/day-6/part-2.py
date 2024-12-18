from typing import List


def find_guard(text: List[str]):
    for y, line in enumerate(text):
        for x, char in enumerate(line):
            if char == "^":
                return [x, y]

    raise Exception("Guard not found")


# up, right, down, left
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
sum = 0


def get_next_direction(current):
    index = directions.index(current)
    return directions[(index + 1) % len(directions)]


def is_loop(og_text: List[str], obstruction_coords: List[int]):
    position = find_guard(og_text)
    direction_headed = directions[0]  # start off going up

    text = [list(line) for line in og_text]

    if text[obstruction_coords[1]][obstruction_coords[0]] != ".":
        return False

    text[obstruction_coords[1]][obstruction_coords[0]] = "#"

    pos_and_dir_list = {
        f"{position[1]},{position[0]},{direction_headed[1]},{direction_headed[0]}": 1
    }

    while True:
        next_position = [
            position[0] + direction_headed[0],
            position[1] + direction_headed[1],
        ]

        # Check if next_position is within bounds
        if not (
            0 <= next_position[1] < len(text)
            and 0 <= next_position[0] < len(text[next_position[1]])
        ):
            return False

        next_char = text[next_position[1]][next_position[0]]

        if next_char != "#":
            position = next_position
        else:
            pos_and_dir = f"{next_position[1]},{next_position[0]},{direction_headed[1]},{direction_headed[0]}"
            if pos_and_dir in pos_and_dir_list:
                return True

            pos_and_dir_list[pos_and_dir] = 1

            direction_headed = get_next_direction(direction_headed)


with open("input.txt", "r") as file:
    og_text = file.read().splitlines()

    for y, line in enumerate(og_text):
        for x, char in enumerate(line):
            print(y)
            if is_loop(og_text, [x, y]):
                sum += 1

print("SUM IS", sum)
