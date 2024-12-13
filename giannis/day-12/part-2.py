with open("sample.txt") as file:
    lines = [list(x) for x in file.read().splitlines()]
    regions = []
    visited = set()

    def get_region(region_to_fill, char, x, y):
        if (x, y) in visited:
            return

        if (
            y >= 0
            and x >= 0
            and y < len(lines)
            and x < len(lines[0])
            and lines[y][x] == char
        ):
            visited.add((x, y))
            region_to_fill.append((char, x, y))

            found = any((char, x, y - 1) in sublist for sublist in regions)

            if not found:
                get_region(region_to_fill, char, x, y - 1)

            found = any((char, x, y + 1) in sublist for sublist in regions)
            if not found:
                get_region(region_to_fill, char, x, y + 1)

            found = any((char, x - 1, y) in sublist for sublist in regions)
            if not found:
                get_region(region_to_fill, char, x - 1, y)

            found = any((char, x + 1, y) in sublist for sublist in regions)
            if not found:
                get_region(region_to_fill, char, x + 1, y)

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            region_to_fill = []
            # fill list with regions of adjacent characters
            get_region(region_to_fill, char, x, y)
            if len(region_to_fill):
                regions.append(region_to_fill)

    regions_sum = 0
    for region in regions:
        perimeter = 0
        area = len(region)

        # keep track of x AND y coordinate, second one is which one was modified to find a border,
        # and which direction it was modified towards
        # i.e. ('y', 3, -1)

        # example:          01
        #          line 0:  EE
        #               1:  E
        #               2:  EE
        # starting from top going counter clockwise
        #

        # up
        # ('0','y',0,-1) -> next visits check to see if already counted
        # left
        # ('0','x',0,-1)
        # down
        # ('0','y',2,+1)
        # right
        # ('2','x',1,+1)
        # up
        # ('1','y',2,-1)
        # right
        # ('1','x',0,+1)
        # down
        # ('1','y',0,+1)
        # right
        # ('0','x',1,+1)

        counted_sides = set()

        for char in region:
            # look on all sides and see if they belong to a different plant.
            # else, doesn't add to perimeter
            x = char[1]
            y = char[2]
            plant = char[0]

            # if changed direction is same, is other direction sequential if yes, then don't add more
            if (y - 1, "x", x, -1) not in counted_sides or (
                y + 1,
                "x",
                x,
                +1,
            ) not in counted_sides:
                if x - 1 >= 0:
                    if lines[y][x - 1] != plant:
                        counted_sides.add((y, "x", x, -1))
                        perimeter += 1
                else:
                    counted_sides.add((y, "x", x, -1))
                    perimeter += 1
                if x + 1 < len(lines[0]):
                    if lines[y][x + 1] != plant:
                        counted_sides.add((y, "x", x, +1))
                        perimeter += 1
                else:
                    counted_sides.add((y, "x", x, +1))
                    perimeter += 1

            if (x - 1, "y", y, -1) or (x + 1, "y", y, +1) not in counted_sides:
                if y - 1 >= 0:
                    if lines[y - 1][x] != plant:
                        counted_sides.add((x, "y", y, -1))
                        perimeter += 1
                else:
                    counted_sides.add((x, "y", y, -1))
                    perimeter += 1
                if y + 1 < len(lines):
                    if lines[y + 1][x] != plant:
                        counted_sides.add((x, "y", y, +1))
                        perimeter += 1
                else:
                    counted_sides.add((x, "y", y, +1))
                    perimeter += 1

        print(region[0][0], "counted sides are", counted_sides)

        # regions_sum += perimeter * area
        # print(regions_sum)
