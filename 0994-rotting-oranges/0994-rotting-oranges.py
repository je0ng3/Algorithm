class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        answer = 0
        m, n = len(grid), len(grid[0])

        # 썩은 오렌지의 위치, 건강한 오랜지 수
        q = collections.deque() 
        count = 0
        for i, row in enumerate(grid):
             count += row.count(1)
             for j, c in enumerate(row):
                  if c==2:
                       q.append((i, j))

        # 확산
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]
        while q and count>0:
            for _ in range(len(q)): # 날짜 구분
                r, c = q.popleft()
                for i in range(4):
                    nr, nc = r+dr[i], c+dc[i]
                    if 0<=nr<m and 0<=nc<n \
                        and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        count -=1
                        q.append((nr, nc))
            answer += 1
        
        if count==0:
            return answer
        return -1