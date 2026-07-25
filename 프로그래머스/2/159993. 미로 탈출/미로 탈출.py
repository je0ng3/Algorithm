from collections import deque

def solution(maps):
    m, n = len(maps), len(maps[0])
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    def bfs(maps, start, end):
        q = deque([start+[0]])
        visited = [[False]*n for _ in range(m)]
        visited[start[0]][start[1]]=True
        while q:
            r, c, time = q.popleft()
            if [r,c]==end:
                return time 
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i] 
                if 0<=nr<m and 0<=nc<n and \
                    not visited[nr][nc] and maps[nr][nc]!='X':
                    visited[nr][nc]=True
                    q.append((nr, nc, time+1))
        return -1
    
    answer = 0
    start = lever = exit = []
    for i in range(m):
        for j in range(n):
            if maps[i][j]=='S':
                start = [i, j]
            elif maps[i][j]=='L':
                lever = [i, j]
            elif maps[i][j]=='E':
                exit=[i,j]
    if not (start and lever and exit):
        return -1
    # S -> L
    temp = bfs(maps, start, lever)
    if temp==-1:
        return -1
    answer += temp
    
    # L -> E
    temp = bfs(maps, lever, exit)
    if temp==-1:
        return -1
    answer += temp
    
    return answer

