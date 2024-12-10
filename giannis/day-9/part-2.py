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
    print(decoded)

    char_lengths = []

    j = len(decoded) - 1
    while j >= 0:
        char = decoded[j]
        contiguous = 1
        while True:
            if char != ".":
                if decoded[j - 1] == char:
                    contiguous += 1
                    j -= 1
                else:
                    j -= 1
                    break
            else:
                j -= 1
                break
        if char != ".":
            char_lengths.append({"char": char, "space": contiguous})

        # iterate through list and look for consecutive free spaces
        num_free = 0

    for idx, each in enumerate(char_lengths):
        print(char_lengths)
        xj = 0
        contiguous_j = 0
        while xj < len(decoded):
            char_j = decoded[xj]
            if char_j == ".":
                contiguous_j += 1
                xj += 1
            else:
                if xj >= 0:
                    if contiguous_j >= each["space"]:
                        # TODO assign correctly
                        decoded[xj - contiguous_j : xj - 1] = [each["char"]] * each[
                            "space"
                        ]
                        char_lengths.pop(idx)
                        print("".join(decoded))
                        break
                xj += 1
