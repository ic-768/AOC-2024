    i = len(decoded) - 1
    while i >= 0:
        char = decoded[i]
        contiguous = 1
        while True:
            if char != ".":
                if decoded[i - 1] == char:
                    contiguous += 1
                    i -= 1
                else:
                    i -= 1
                    break
            else:
                i -= 1
                break
        print(contiguous, char)
