class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        grid = {}
        for i in range(3):
            for j in range(3):
                grid[(i,j)] = {}
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r] or val in cols[c] or val in grid[(r//3, c//3)]:
                    return False
                rows[r][val] = 1
                cols[c][val] = 1
                grid[(r//3, c//3)][val] = 1
        return True