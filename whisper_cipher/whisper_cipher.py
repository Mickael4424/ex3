def Shift_alphabet(string1: str, n: int):
    result = []
    for s in string1:
        if s.isalpha():
            if s.islower():
                shifted = (ord(s) - ord('a') + n) % 26
                result.append(chr(ord('a') + shifted))
            else:
                shifted = (ord(s) - ord('A') + n) % 26
                result.append(chr(ord('A') + shifted))
        else:
            result.append(s)
    return "".join(result)


def main():

    print("Test:")
    print("# Basic cases")
    print(Shift_alphabet("abz", 1))

    print(Shift_alphabet("AbZ", 1))

    print("# With spaces and punctuation")
    print(Shift_alphabet("Hello World!", 3))

    print("# Negative shift")
    print(Shift_alphabet("bca", -1))

    print("# Large shift (wrap around)")
    print(Shift_alphabet("abc", 26))

    print(Shift_alphabet("xyz", 3))

    print("# Mixed characters")
    print(Shift_alphabet("Python 3.8!", 5))

    print("# Edge cases")
    print(Shift_alphabet("", 10))

    print(Shift_alphabet("12345", 4))


if __name__ == "__main__":
    main()
