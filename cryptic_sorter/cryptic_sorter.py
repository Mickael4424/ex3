def count_vowels(word: str):
    vowels = "aeiou"
    return sum(1 for c in word.lower() if c in vowels)


def Sort_string(tlist: list[str]):
    return sorted(
        tlist,
        key=lambda s: (
            count_vowels(s),
            len(s),
            s.lower(),
            s
        )
    )


def main():

    print("\n# Basic cases")
    print(Sort_string(["apple", "bat", "car", "ae", "b"]))

    print("\n# Same vowel count, different lengths")
    print(Sort_string(["dog", "cat", "hi", "a"]))

    print("\n# Same vowel count and length → lexicographical order")
    print(Sort_string(["bat", "cat", "ant"]))

    print("\n# Mixed uppercase and lowercase")
    print(Sort_string(["Apple", "banana", "Kiwi", "grape"]))

    print("\n# Sorted by vowel count (case-insensitive)")

    print("\n# Edge cases")
    print(Sort_string([]))
    print(Sort_string(["a", "e", "i", "o", "u"]))
    print(Sort_string(["bbb", "ccc", "ddd"]))


if __name__ == "__main__":
    main()
