class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    for r0 in range(row):
                        if matrix[r0][c] != 0:
                            matrix[r0][c] = -1
                    for c0 in range(col):
                        if matrix[r][c0] != 0:
                            matrix[r][c0] = -1
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == -1:
                    matrix[r][c] = 0
        
        