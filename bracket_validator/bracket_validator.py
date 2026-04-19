def bracket_validator(bracket: str):
    text = f"bracket_validator({bracket})"
    print(text, end="")
    print(" " * (50 - len(text)), end="")

    bracket_open = "(", "{", "["
    bracket_close = ")", "}", "]"

    list = []
    i = 0
    while i < len(bracket):
        if bracket[i] in bracket_open:
            list.append(bracket[i])
        elif bracket[i] in bracket_close:
            if not list:
                print("# False")
                return False
            t = list.pop()
            if bracket[i] == '}' and t != '{':
                print("# False")
                return False
            elif bracket[i] == ')' and t != '(':
                print("# False")
                return False
            elif bracket[i] == ']' and t != '[':
                print("# False")
                return False
        i += 1
    if len(list) == 0:
        print("# True")
        return
    else:
        print("# False")
        return


def main():
    print("Test")
    print("\n# Valid cases")
    bracket_validator("()")
    bracket_validator("()[]{}")
    bracket_validator("{[()]}")
    bracket_validator("")
    bracket_validator("hello(hhhh)world{ho}w are")

    print("\n# Invalid cases")
    bracket_validator("(]")
    bracket_validator("([)]")
    bracket_validator("(((")
    bracket_validator("())")
    bracket_validator("{[(])}")


if __name__ == "__main__":
    main()
