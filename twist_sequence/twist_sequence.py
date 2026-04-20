def twister(list1: list, n: int):
    if not list1:
        return list1
    i = 0
    n = n % len(list1)
    while i < n:
        item_removed = list1.pop()
        list1 = [item_removed] + list1
        i += 1
    return list1


def main():

    print("Test:")
    print("# Basic cases")
    print(twister([1, 2, 3, 4, 5], 2))

    print(twister([4, 2, 1, -1, 'a'], 4))

    print("# Rotation equal to length")
    print(twister([1, 2, 3], 3))

    print("# Rotation greater than length")
    print(twister([1, 2, 3], 5))

    print("# Negative rotation (left rotation)")
    print(twister([1, 2, 3, 4], -1))

    print("# Edge cases")
    print(twister([], 3))
    print(twister([1], 10))


if __name__ == "__main__":
    main()
