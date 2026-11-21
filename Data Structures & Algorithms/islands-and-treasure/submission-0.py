class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                nr, nc = r+dr, c+dc #newrow, newcol = r + directionrow, c + directioncol
                if (
                    nr < 0 or nr == ROWS or
                    nc < 0 or nc == COLS or
                    grid[nr][nc] != INF
                ): continue
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr,nc))
        
