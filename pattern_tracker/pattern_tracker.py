def Pattern_tracker(text: str):
    print(f'print(Pattern_tracker("{text}"))')
    return sum(
        1
        for i in range(1, len(text))
        if text[i - 1].isdigit()
        and text[i].isdigit()
        and int(text[i]) == int(text[i - 1]) + 1
    )


def main():
    print("Test:")

    print("\n# Basic cases")
    print(Pattern_tracker("123a345"))
    print(Pattern_tracker("1a2b3c4d5"))

    print("\n# Mixed complex case")
    print(Pattern_tracker("12asd34hkh45kjhj56jhj67kjhjh78kjhjh89kjhkhj110"))

    print("\n# Edge cases")
    print(Pattern_tracker(""))
    print(Pattern_tracker("7"))
    # print(answer.Pattern_tracker("111111"))
    print(Pattern_tracker("012345"))
    print(Pattern_tracker("98"))


if __name__ == "__main__":
    main()
