def solution(n, s, a, b, fares):
    INF = float('inf')
    answer = INF
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        graph[i][i] = 0
    for n1, n2, f in fares:
        graph[n1][n2]=f
        graph[n2][n1]=f
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    for i in range(1, n+1):
        total = graph[s][i]+graph[i][a]+graph[i][b]
        answer = min(total, answer)
    return answer