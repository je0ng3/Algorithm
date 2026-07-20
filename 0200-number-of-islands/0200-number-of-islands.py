class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(grid, r, c):
            grid[r][c] = '0'
            dr = [0,0,1,-1]
            dc = [1,-1,0,0]
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]=='1':
                    dfs(grid, nr, nc)
            
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    dfs(grid, r, c)
                    count += 1
        
        return count