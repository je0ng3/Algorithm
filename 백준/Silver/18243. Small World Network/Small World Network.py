import sys

INF = int(1e9)
n, k = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(k):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

big = False
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

if not big:
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] == INF or graph[a][b]>6:
                big = True
                break

if big:
    print("Big World!")
else:
    print("Small World!")
        
