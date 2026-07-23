import collections

def solution(maps):
    answer = 0
    # 최단거리 s -> e
    def bfs(maps, s, e):
        m = len(maps)
        n = len(maps[0])
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]
        q = collections.deque()
        q.append((s[0], s[1], 0))
        visited = [[False]*n for _ in range(m)]
        visited[s[0]][s[1]] = True
        while q:
            r, c, t = q.popleft()
            if [r, c]==e:
                return t
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0<=nr<m and 0<=nc<n \
                    and maps[nr][nc]!='X' and not visited[nr][nc]:
                    visited[nr][nc]=True
                    q.append((nr,nc,t+1))
        return -1
    
    start = exit = lever = []
    for r, ms in enumerate(maps):
        for c, m in enumerate(ms):
            if m=='S':
                start = [r, c]
            elif m=='E':
                exit = [r, c]
            elif m=='L':
                lever = [r, c]
        if start and exit and lever:
            break
    if not (start and exit and lever):
        return -1
    
    # 레버
    time = bfs(maps, start, lever)
    if time==-1:
        return time
    answer += time
    
    # 출구
    time = bfs(maps, lever, exit)
    if time==-1:
        return time
    answer += time    
    
    return answer