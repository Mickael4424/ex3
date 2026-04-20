def sculptor(string1: str):
    result = []
    lower = True
    for char in string1:
        if char.isalpha():
            if lower:
                result.append(char.lower())
                lower = False
            else:
                result.append(char.upper())
                lower = True
        else:
            result.append(char)
    return "".join(result)


def main():

    print("Test:")

    print("# Basic case")
    print(sculptor("Hello world"))

    print("# With punctuation")
    print(sculptor("Hello, world!"))

    print("# With numbers")
    print(sculptor("123abcDEF"))

    print("# Mixed characters")
    print(sculptor("a-bC-dEf-ghIj"))

    print("# Edge cases")
    print(sculptor(""))

    print(sculptor("12345"))

    print(sculptor("A"))

    print(sculptor("ab"))


if __name__ == "__main__":
    main()
