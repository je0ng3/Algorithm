from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            grid[row][col] = "0"
            stack = deque([(row, col)])
            while stack:
                cr, cc = stack.pop()
                for dr, dc in [(0,1), (1,0), (0,-1),(-1,0)]:
                    nr, nc = cr+dr, cc+dc
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]=="1":
                        grid[nr][nc]="0"
                        stack.append((nr,nc))
            return 
        
        lslands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    dfs(r, c)
                    lslands += 1
        
        return lslands