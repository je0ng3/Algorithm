from collections import deque

def solution(maps):
    answer = bfs(0,0,maps)
    return answer

def bfs(r,c, graph):
    dr = [0,0,1,-1]
    dc = [1,-1, 0,0]
    queue = deque([(r,c)])
    visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]
    while queue:
        (r, c) = queue.popleft()
        visited[r][c] = True
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<len(graph) and 0<=nc<len(graph[0]):
                if (not visited[nr][nc]) and graph[nr][nc]==1:
                    graph[nr][nc] = graph[r][c]+1
                    if nr == len(graph)-1 and nc == len(graph[0])-1:
                        return graph[nr][nc]
                    visited[nr][nc] = True
                    queue.append((nr, nc))
    return -1