with open("input.txt") as file:
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

        for char in region:
            # look on all sides and see if they belong to a different plant.
            # else, doesn't add to perimeter
            x = char[1]
            y = char[2]
            plant = char[0]

            # left side
            if x - 1 < 0 or lines[y][x - 1] != plant:
                perimeter += 1

            # right side
            if x + 1 >= len(lines[0]) or lines[y][x + 1] != plant:
                perimeter += 1

            # top side
            if y - 1 < 0 or lines[y - 1][x] != plant:
                perimeter += 1

            # bottom side
            if y + 1 >= len(lines) or lines[y + 1][x] != plant:
                perimeter += 1

        regions_sum += perimeter * area
        print(regions_sum)
