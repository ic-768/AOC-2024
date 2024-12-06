from typing import List


def find_guard(text: List[str]) -> List[int]:
    for y, line in enumerate(text):
        for x, char in enumerate(line):
            if char == "^":
                return [x, y]

    raise Exception("Guard not found")


# up, right, down, left
directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]


def get_next_direction(current: List[int]) -> List[int]:
    index = directions.index(current)
    return directions[(index + 1) % len(directions)]


with open("input.txt", "r") as file:
    text = file.read().split()
    position = find_guard(text)
    visited = {f"{position[0]},{position[1]}": 1}
    direction_headed = directions[0]  # start off going up

    while True:
        try:
            next_position = [
                position[0] + direction_headed[0],
                position[1] + direction_headed[1],
            ]

            next_char = text[next_position[1]][next_position[0]]

            if next_char != "#":
                visited[f"{next_position[1]},{next_position[0]}"] = 1
                position = next_position
            else:
                direction_headed = get_next_direction(direction_headed)

        except Exception:
            print(len(visited))
            break
