from collections import defaultdict

def solution(N, road, K):
    answer = 0
    INF = float('inf')
    dist = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        dist[i][i] = 0
    for u, v, w in road:
        w = min(dist[u][v], w)
        dist[u][v] = w
        dist[v][u] = w
    for k in range(N+1):
        for i in range(N+1):
            for j in range(N+1):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    for i in range(1, N+1):
        if dist[1][i]<=K:
            answer += 1
    return answer