class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        answer = 0
        m, n = len(grid), len(grid[0])
        q = deque() # 썩은 오렌지
        count = 0 # 멀쩡한 오렌지 수
        for i in range(m):
            count += grid[i].count(1)
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i, j))
        if count==0:
            return 0
        # 확산
        dirs = ((1,0),(-1,0),(0,1),(0,-1))
        while q and count:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<m and 0<=nc<n \
                        and grid[nr][nc]==1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        count -=1
            answer += 1
        if count>0:
            return -1
        return answer