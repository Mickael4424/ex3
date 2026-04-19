def reverseMatrix(matrix: list):
    text = f'reverseMatrix({matrix})'
    print(text)
    new_matrix = [row[::-1] for row in matrix]
    print(new_matrix)
    return new_matrix


def main() -> None:
    print("Test")

    print("\n# Basic cases")
    reverseMatrix([[1, 2], [3, 4]])
    print()
    reverseMatrix([[1, 2, 3], [4, 5, 6]])

    print("\n# Single row")
    reverseMatrix([[1, 2, 3, 4]])

    print("\n# Single column")
    reverseMatrix([[1], [2], [3]])

    print("\n# Edge cases")
    reverseMatrix([[1]])

    print("\n# Larger matrix")
    reverseMatrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])


if __name__ == "__main__":
    main()
