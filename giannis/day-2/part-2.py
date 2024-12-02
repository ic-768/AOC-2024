list1 = []
list2 = []

with open("input.txt", "r") as file:
    lines = file.readlines()
    num_safe_reports = 0

for line in lines:
    elements = [int(x) for x in line.split()]
    safe_threshold = 1
    asc_direction = None  # True for asc, False for desc

    prev_element = None
    for element in elements:
        if safe_threshold < 0:
            break

        if prev_element is None:
            prev_element = element
        else:
            diff = abs(prev_element - element)
            is_ascending = prev_element < element

            if asc_direction is None:
                asc_direction = is_ascending

            elif is_ascending != asc_direction:
                safe_threshold -= 1
                if safe_threshold < 0:
                    break

            prev_element = element
            if asc_direction is not None:
                if diff < 1 or diff > 3:
                    safe_threshold -= 1
                    if safe_threshold < 0:
                        break

    if safe_threshold >= 0:
        num_safe_reports += 1

print(num_safe_reports)
