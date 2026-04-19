def is_palindrome(string: str):
    text = f'is_palindrome("{string}")'
    print(text + " " * max(1, 50 - len(text)), end="")

    cleaned = "".join(c.lower() for c in string if c.isalnum())

    i, j = 0, len(cleaned) - 1

    while i < j:
        if cleaned[i] != cleaned[j]:
            print("False")
            return False
        i += 1
        j -= 1
    print("True")
    return True


def main() -> None:
    print("Test:")

    print("\n# Valid cases")
    is_palindrome("madam")
    is_palindrome("racecar")
    is_palindrome("A man, a plan, a canal: Panama")
    is_palindrome("No 'x' in Nixon")
    is_palindrome("")
    is_palindrome("a")

    print("\n# Invalid cases")
    is_palindrome("hello")
    is_palindrome("python")
    is_palindrome("OpenAI")

    print("\n# Edge cases")
    is_palindrome("12321")
    is_palindrome("12345")
    is_palindrome("Able was I ere I saw Elba")


if __name__ == "__main__":
    main()
