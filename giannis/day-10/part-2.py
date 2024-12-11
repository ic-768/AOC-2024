def traverse_trails(point, value, returned):
    x = point["x"]
    y = point["y"]

    neighbors = [
        {"x": x + 1, "y": y},
        {"x": x - 1, "y": y},
        {"x": x, "y": y + 1},
        {"x": x, "y": y - 1},
    ]

    neighbors = [i for i in neighbors if 0 <= i["x"] < l_x and 0 <= i["y"] < l_y]
    neighbors = [i for i in neighbors if int(file[i["y"]][i["x"]]) == value + 1]

    if value == 8:
        return len(neighbors)

    else:
        return sum(traverse_trails(p, value + 1, returned) for p in neighbors)


with open("input.txt") as f:
    file = f.read().split("\n")
    file = [list(i) for i in file]
    l_y = len(file) - 1
    l_x = len(file[0])

    total_sum = 0
    for y, line in enumerate(file):
        for x, char in enumerate(line):
            if char == "0":
                point = {"x": x, "y": y}
                total_sum += traverse_trails(point, 0, [])


print(total_sum)
