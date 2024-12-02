def read_input(file_path):
    """Reads and parses the input file for Advent of Code problem."""
    with open(file_path, 'r') as file:
        lines = file.readlines()

    left_list = []
    right_list  = []
    for line in lines:
        for index, number in enumerate(line.split()):
            if index % 2 :
                right_list.append(int(number))
            else:
                left_list.append(int(number))

    return left_list, right_list


def calculate_total_distance(left_list: list[int], right_list: list[int]) -> int:

    return sum(abs(a - b) for a, b in zip(left_list, right_list))



if __name__ == "__main__":
    # Example input lists. Replace these with actual input values.
    left_list, right_list = read_input('input.txt')

    left_list.sort()
    right_list.sort()

    # Calculate and print the total distance
    total_distance = calculate_total_distance(left_list, right_list)
    print(f"Total distance: {total_distance}")
