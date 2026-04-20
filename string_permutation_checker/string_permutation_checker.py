def Anagram(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    else:
        if sorted(s1) == sorted(s2):
            print(sorted(s1))
            print(sorted(s2))
            return True
        else:
            return False


def main():

    print("Test:")
    print(Anagram("racecar", "carrace"))
    print(Anagram("racecar", "carace"))
    print(Anagram("Conversation", "Voices rant on"))


if __name__ == "__main__":
    main()
