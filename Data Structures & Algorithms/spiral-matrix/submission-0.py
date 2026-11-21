class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS,COLS = len(matrix), len(matrix[0])
        visit = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]] # move right, down, left, up
        i = 0
        result = []
        row = 0
        col = 0
        def check_valid(row,col):
            if (row,col) in visit or row<0 or col<0 or row == ROWS or col == COLS:
                return False
            return True
        while len(result) < ROWS*COLS:
            visit.add((row,col))
            result.append(matrix[row][col])
            if len(result) == ROWS*COLS:
                return result
            dr, dc = directions[i%4]
            nr, nc = row+dr, col + dc
            check_valid(nr,nc)
            while not check_valid(nr, nc):
                i+= 1
                dr, dc = directions[i%4]
                nr, nc = row+dr, col + dc
            row = nr
            col = nc
            
        return result