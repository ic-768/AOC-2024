with open("sample.txt", "r") as file:
    text = file.read().splitlines()[0]
    char_number = 0

    decoded = []
    for x, char in enumerate(text):
        not_free = x % 2 == 0

        if not_free:
            # we don't use .extend because it would combine multi-digit numbers into one entry
            for num in range(int(char)):
                # append them as many times as needed
                decoded.append(str(char_number))
            char_number += 1

        else:
            decoded.extend("." * int(char))

    # iterate from end of the list
    decoded = list("00...111...2....888899")
    last_checked = len(decoded) - 1
    while last_checked > 0:
        try:
            first_free = decoded.index(".")
            if last_checked < first_free:
                break
        except:
            break

        for i in range(len(decoded) - 1, -1, -1):
            # if empty space continue
            num = decoded[i]
            if num == ".":
                continue

            # how many same numbers in a row
            num_contiguous = 1

            # iterate through a block of same numbers
            # look at next numbers and determine if they fit

            while True:
                last_checked -= 1
                if decoded[i - num_contiguous] == num:
                    num_contiguous += 1
                else:
                    break

            if last_checked <= 0:
                break

            # iterate through list and look for consecutive free spaces
            num_free = 0

            print("".join(decoded))
            for x in range(len(decoded)):
                if decoded[x] == "." and x < i:
                    num_free += 1
                    if num_free == num_contiguous:
                        decoded[x - num_contiguous + 1 : x + 1] = [
                            str(num)
                        ] * num_contiguous
                        decoded[i - num_contiguous + 1 : i + 1] = ["."] * num_contiguous
                        num_free = 0
                        break
                else:
                    num_free = 0
