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
    for y, region in enumerate(regions):
        perimeter = 0
        area = len(region)

        # check to find corners and add them instead of sides
        # corner if : nothing top, left
        #             nothing top, right
        #             nothing bottom, left
        #             nothing bottom, right

        # AAAAA
        # BBCCC
        # BBCCC
        # EEECC

        for char in region:
            x = char[1]
            y = char[2]
            plant = char[0]

            nothing_left = (x - 1 < 0) or (lines[y][x - 1] != plant)
            nothing_top = (y - 1 < 0) or (lines[y - 1][x] != plant)
            nothing_right = (x + 1 >= len(lines[0])) or (lines[y][x + 1] != plant)
            nothing_bottom = (y + 1 >= len(lines)) or (lines[y + 1][x] != plant)

            nothing_bottom_left = (
                (y + 1 >= len(lines) or x - 1 < 0 or lines[y + 1][x - 1] != plant)
                and (x - 1 < 0 or lines[y][x - 1] != plant)
                and (y + 1 >= len(lines) or lines[y + 1][x] != plant)
            )

            nothing_bottom_right = (
                (
                    y + 1 >= len(lines)
                    or x + 1 >= len(lines[0])
                    or lines[y + 1][x + 1] != plant
                )
                and (x + 1 >= len(lines[0]) or lines[y][x + 1] != plant)
                and (y + 1 >= len(lines) or lines[y + 1][x] != plant)
            )

            nothing_top_left = (
                (y - 1 < 0 or x - 1 < 0 or lines[y - 1][x - 1] != plant)
                and (x - 1 < 0 or lines[y][x - 1] != plant)
                and (y - 1 < 0 or lines[y - 1][x] != plant)
            )

            nothing_top_right = (
                # top-right is out of bounds or another plant
                (y - 1 < 0 or x + 1 >= len(lines[0]) or lines[y - 1][x + 1] != plant)
                and
                # no/different plant directly to the right
                (
                    (x + 1 >= len(lines[0]) or lines[y][x + 1] != plant)
                    # no/different plant directly above
                    and (y - 1 < 0 or lines[y - 1][x] != plant)
                )
                # no/different plant directly to the top
                and (y - 1 < 0 or lines[y - 1][x] != plant)
            )

            inverted_top_right = (
                # top-right is out of bounds or another plant
                (y - 1 < 0 or x + 1 >= len(lines[0]) or lines[y - 1][x + 1] != plant)
                # Check for L shape ( one above and one to the right
                and (x + 1) < len(lines[0])
                and y - 1 >= 0
                and lines[y][x + 1] == plant
                and lines[y - 1][x] == plant
            )

            inverted_top_left = (
                # top-left is out of bounds or another plant
                (y - 1 < 0 or x - 1 < 0 or lines[y - 1][x - 1] != plant)
                # Check for L shape ( one above and one to the left
                and x - 1 >= 0
                and y - 1 >= 0
                and lines[y][x - 1] == plant
                and lines[y - 1][x] == plant
            )

            # shouldn't have something to it's right OR also have something above it

            if nothing_bottom_left:
                # print("bottom-left")
                perimeter += 1

            if nothing_bottom_right:
                # print("bottom-right")
                perimeter += 1

            if nothing_top_left:
                # print("top-left")
                perimeter += 1

            if nothing_top_right:
                # print("top-right")
                perimeter += 1

            if inverted_top_right:
                print(char)
                print("inverted top-right")
                perimeter += 1
        regions_sum += perimeter * area
