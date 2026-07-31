from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    maps = [[0]*102 for _ in range(102)]
    # 맵에 직사각형 그리기
    for r1, c1, r2, c2 in rectangle:
        for r in range(r1*2, r2*2+1):
            for c in range(c1*2, c2*2+1):
                maps[r][c] = 1
    # 둘레만 남기고 선 제거
    for r1, c1, r2, c2 in rectangle:
        for r in range(r1*2+1, r2*2):
            for c in range(c1*2+1, c2*2):
                maps[r][c] = 0
    # 아이템 줍는 최단 경로
    def bfs(sr, sc, ir, ic):
        q = deque([(sr, sc, 0)])
        visited = set()
        visited.add((sr, sc))
        while q:
            r, c, dist = q.popleft()
            if (r, c)==(ir, ic):
                return dist//2
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r+dr, c+dc
                if maps[nr][nc]==1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, dist+1))
    
    answer = bfs(characterX*2, characterY*2, itemX*2, itemY*2)
    return answer