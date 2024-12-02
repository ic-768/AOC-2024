def is_safe(list_row: list) -> bool:
    increase = True
    decrease = True

    for i in range(len(list_row) - 1):

        current_element = int(list_row[i])
        next_element = int(list_row[i + 1])


        if (current_element - next_element) in (-1, -2, -3):
            decrease = False

        elif (current_element - next_element) in (1, 2, 3):
            increase = False

        else:
            return False


    if (increase and not decrease) or (not increase and decrease):
        return True
    return False


def run_main(file_path):
    with open(file_path, 'r') as data:
        count = 0
        while True:
            # Read a line from the data
            line = data.readline()
            if not line:
                break
            row_list = list(line.rstrip().split(' '))
            if is_safe(row_list):
                count = count + 1

    print(f"Count: {count}")

if __name__ == "__main__":

    run_main('input.txt')    # Calculate and print the total distance
