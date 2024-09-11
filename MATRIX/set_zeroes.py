class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:

                    # coat r row with 2's except that which is 0 
                    for uc in range(cols):
                        if matrix[r][uc] != 0:
                            matrix[r][uc] = 'a' 
                    for ur in range(rows):
                        if matrix[ur][c] != 0:
                            matrix[ur][c] = 'a' 

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 'a':
                    matrix[r][c] = 0