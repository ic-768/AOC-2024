def get_neighbors(point, value, returned):
    global total_num_9

    x = point["x"]
    y = point["y"]

    points = [
        {"x": x + 1, "y": y},
        {"x": x - 1, "y": y},
        {"x": x, "y": y + 1},
        {"x": x, "y": y - 1},
    ]
    points = [i for i in points if 0 <= i["x"] < l_x and 0 <= i["y"] < l_y]
    points = [i for i in points if int(file[i["y"]][i["x"]]) == value + 1]

    if value == 8:
        total_num_9 += len(points)

        unique_points = [i for i in points if i not in unique_num_9]
        unique_num_9.extend(unique_points)

    else:
        [get_neighbors(p, value + 1, returned) for p in points]


total_unique_num_9 = 0
total_num_9 = 0

with open("input.txt") as f:
    file = f.read().split("\n")
    file = [list(i) for i in file]
    l_y = len(file) - 1
    l_x = len(file[0])

    for y, line in enumerate(file):
        for x, char in enumerate(line):
            unique_num_9 = []
            if char == "0":
                point = {"x": x, "y": y}
                get_neighbors(point, 0, [])
                total_unique_num_9 += len(unique_num_9)


print(total_unique_num_9)
print(total_num_9)

