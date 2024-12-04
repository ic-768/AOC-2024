from typing import List


def find_occurrences(text: str):
    return text.count("XMAS")


def generate_diag_lines(lines: List[str]):
    diagonals_1 = []
    diagonals_2 = []

    # iterate upwards on left-most column
    for i in range(len(lines) - 1, -1, -1):
        row, col = i, 0
        line = []
        while col < len(lines) and row < len(lines):
            line.append(lines[row][col])
            row += 1
            col += 1
        diagonals_1.append(line)

    # iterate towards the right on top row
    for i in range(len(lines) - 1):
        # +1 to skip main diagonal (covered by previous iteration)
        row, col = 0, i + 1
        line = []
        while col < len(lines) and row < len(lines):
            line.append(lines[row][col])
            row += 1
            col += 1
        diagonals_1.append(line)

    # iterate downwards on left-most column
    for i in range(len(lines)):
        row, col = i, 0
        line = []
        while col < len(lines) and row >= 0:
            line.append(lines[row][col])
            row -= 1
            col += 1

        diagonals_2.append(line)

    # iterate towards the left on bottom row
    # -2 in range, and +1 to i to skip main diagonal again
    for i in range(len(lines) - 2, -1, -1):
        row, col = len(lines) - 1, i + 1
        line = []
        while row < len(lines) and col < len(lines):
            line.append(lines[row][col])
            row -= 1
            col += 1
        diagonals_2.append(line)

    return ["".join(line) for line in diagonals_1], [
        "".join(line) for line in diagonals_2
    ]


with open("input.txt", "r") as file:
    horiz = file.read().splitlines()
    vert = ["".join(t) for t in zip(*horiz)]
    diag1, diag2 = generate_diag_lines(horiz)

    horiz_rev = [item[::-1] for item in horiz]
    vert_rev = [item[::-1] for item in vert]
    diag1_rev = [item[::-1] for item in diag1]
    diag2_rev = [item[::-1] for item in diag2]

    # reverse each string array. We can't just reverse the whole thing because then we get false positives

    sum = 0
    for each in [
        horiz,
        vert,
        diag1,
        diag2,
        horiz_rev,
        vert_rev,
        diag1_rev,
        diag2_rev,
    ]:
        for item in each:
            sum += find_occurrences(item)
    print(sum)
