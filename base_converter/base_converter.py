
def converts_base(value: str, origin_base, dest_base):

    if not (2 <= origin_base <= 36 and 2 <= dest_base <= 36):
        raise ValueError("Base must be between 2 and 36")

    value = value.strip().upper()
    text = f'converts_base("{value}", {origin_base}, {dest_base})'
    print(text, end="")
    print(" " * (50 - len(text)), end="")

    if value == "" or all(c == '0' for c in value):
        print('# "0"')
        return

    valid_char = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    allowed = valid_char[:origin_base]
    for c in value:
        if c not in allowed:
            print("# Error / invalid digit")
            return

    decimal_value = int(value, origin_base)
    if decimal_value == 0:
        print('# "0"')
        return

    result = []
    while decimal_value > 0:
        remainder = decimal_value % dest_base
        result.append(valid_char[remainder])
        decimal_value //= dest_base
    result = ''.join(reversed(result))
    print(f'# "{result}"')
    return result


def main():

    print("Test:")

    print("\n# Basic conversions")
    converts_base("1010", 2, 10)
    converts_base("10", 10, 2)
    converts_base("1A", 16, 10)
    converts_base("26", 10, 16)

    print("\n# Same base")
    converts_base("123", 10, 10)

    print("\n# Edge cases")
    converts_base("0", 10, 2)
    converts_base("000", 2, 10)

    print("\nLarger bases")
    converts_base("ZZZ", 36, 10)
    converts_base("46655", 10, 36)

    print("\nUppercase handling")
    converts_base("A", 16, 10)
    converts_base("F", 16, 10)

    print("\nMixed digits and letters")
    converts_base("1F4", 16, 10)
    converts_base("500", 10, 16)

    print("\nInvalid cases")
    converts_base("2", 2, 10)
    converts_base("G", 16, 10)


if __name__ == "__main__":
    main()
