def is_safe(report):
    asc_direction = None  # True for ascending, False for descending
    prev_element = report[0]

    for element in report[1:]:
        diff = element - prev_element
        is_ascending = diff > 0

        if asc_direction is None:
            asc_direction = is_ascending

        if asc_direction != is_ascending or abs(diff) < 1 or abs(diff) > 3:
            return False
        prev_element = element

    return True


def can_be_made_safe(report):
    for i in range(len(report)):
        # Create a new list without the i-th element
        modified_report = report[:i] + report[i + 1 :]
        if is_safe(modified_report):
            return True
    return False


num_safe_reports = 0

with open("input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    report = [int(x) for x in line.split()]

    if is_safe(report) or can_be_made_safe(report):
        num_safe_reports += 1

print(num_safe_reports)
