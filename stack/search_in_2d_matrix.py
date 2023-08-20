"""ADS_CSCSC01/stack/search_in_2d_matrix.py
Class Work:

1. Implement: Searching in a 2D matrix for a word, if present return the position of each letter.
"""

class SearchIn2D:

    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.directions = [
            [-1, 0], [1, 0], [1, 1],
            [1, -1], [-1, -1], [-1, 1],
            [0, 1], [0, -1]
        ]


    def search_in_2d(self, target):
        for start_row in range(self.rows):
            for start_col in range(self.cols):
                for direction in self.directions:
                    dr, dc = direction
                    r, c = start_row, start_col
                    found = True

                    for char in target:
                        if not (0 <= r < self.rows and 0 <= c < self.cols and self.matrix[r][c] == char):
                            found = False
                            break
                        r += dr
                        c += dc

                    if found:
                        return [(start_row, start_col), (r - dr, c - dc)]           # returning start and the end position


if __name__ == '__main__':

    matrix = [
        ['A', 'B', 'C', 'T', 'S'],
        ['X', 'G', 'X', 'H', 'O'],
        ['Y', 'Y', 'O', 'E', 'O'],
        ['M', 'Z', 'K', 'O', 'R'],
        ['P', 'L', 'M', 'X', 'D'],
    ]

    target = 'GOOD'
    solution = SearchIn2D(matrix)
    result = solution.search_in_2d(target)
    print(result)
