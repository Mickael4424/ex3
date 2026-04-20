class Solution:
    @staticmethod
    def mergeList(list1, list2):
        if list1 is None:
            list1 = []
        if list2 is None:
            list2 = []
        merged = list1 + list2
        merged.sort()
        merged.reverse()
        return merged


def main():

    print("Test:")

    answer = Solution()

    print("# Basic cases")
    print(answer.mergeList([1, 3, 5, -1], [0, 8, 2, 1]))

    print(answer.mergeList([99, -22, 10, 9], []))

    print("# Both lists non-empty")
    print(answer.mergeList([4, 2], [1, 3]))

    print("# One list is None")
    print(answer.mergeList(None, [5, 3, 1]))

    print(answer.mergeList([7, 6, 8], None))

    print("# Edge cases")
    print(answer.mergeList([], []))

    print(answer.mergeList([1, 1, 1], [1, 1]))

    print(answer.mergeList([-5, -2], [-3, -1]))


if __name__ == "__main__":
    main()
