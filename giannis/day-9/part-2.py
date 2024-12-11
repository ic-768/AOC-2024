with open("input.txt", "r") as file:
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
            char_lengths.append({"char": char, "space": contiguous, "idx": j})

        # iterate through list and look for consecutive free spaces
        num_free = 0

    for idx, each in enumerate(char_lengths):
        space_index = 0
        contiguous_space = 0
        while space_index < len(decoded):
            char_j = decoded[space_index]
            if char_j == ".":
                contiguous_space += 1
                space_index += 1
            else:
                # if free space is after index of char we are done
                if space_index - 1 > each["idx"]:
                    break

                if space_index >= 0:
                    if contiguous_space >= each["space"]:
                        # replace
                        decoded[
                            space_index - contiguous_space : space_index
                            - contiguous_space
                            + each["space"]
                        ] = [each["char"]] * each["space"]

                        decoded[each["idx"] + 1 : each["idx"] + each["space"] + 1] = [
                            "."
                        ] * each["space"]

                        contiguous_space = 0
                        break
                contiguous_space = 0
                space_index += 1

sum = 0

for i, each in enumerate(decoded):
    if each != ".":
        sum += int(each) * i
print(sum)
