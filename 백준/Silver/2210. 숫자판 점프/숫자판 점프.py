from collections import deque

def bfs(i, j):
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]

    q = deque()
    q.append((i, j, str(board[i][j])))
    result = set()
    while q:
        r, c, s = q.popleft()
        if len(s) == 6:
            result.add(s)
            continue
        
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0<=nr<5 and 0<=nc<5:
                q.append((nr, nc, s+str(board[nr][nc])))
    return result

board = [list(map(int, input().split())) for _ in range(5)]

nums = set()
for i in range(5):
    for j in range(5):
        nums |= bfs(i, j)

print(len(nums))


