def solution(n, s, a, b, fares):
    INF = float('inf')
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i][i] = 0
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    answer = graph[s][a]+graph[s][b]
    for i in range(1,n+1):
        if i==s:
            continue
        temp = graph[s][i]
        temp += graph[i][a] if i!=a else 0
        temp += graph[i][b] if i!=b else 0
        answer = min(answer, temp)
    return answer