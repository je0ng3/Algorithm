def solution(n, results):
    answer = 0    
    win = {i:[] for i in range(1, n+1)}
    lose = {i:[] for i in range(1, n+1)}
    for a, b in results:
        win[a].append(b)
        lose[b].append(a)

    def dfs(graph, start):
        stack = [start]
        visited = [False]*(n+1)
        visited[start] = True
        cnt = 0

        while stack:
            cur = stack.pop()
            for nxt in graph[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    cnt += 1
                    stack.append(nxt)

        return cnt 

    for i in range(1, n+1):
        if dfs(win, i)+dfs(lose, i)==n-1:
            answer += 1
    return answer