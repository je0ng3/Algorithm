from collections import deque


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def bfs(y, x, visited, hight):
    visited[y][x] = 1
    que = deque()
    que.append((y, x))
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= ny < n and 0 <= nx < n):
                continue
            if graph[ny][nx] <= hight:
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = 1
                que.append((ny, nx))


min_val = min(map(min, graph))
max_val = max(map(max, graph))

max_area = 1
for hight in range(min_val, max_val):
    visited = [[0] * n for _ in range(n)]
    count = 0
    for j in range(n):
        for k in range(n):
            if visited[j][k] != 1 and graph[j][k] > hight:
                count += 1
                bfs(j, k, visited, hight)
    max_area = max(max_area, count)

print(max_area)