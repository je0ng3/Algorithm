def solution(k, dungeons):
    answer = -1
    visited = [False]*len(dungeons)
    def dfs(power):
        nonlocal answer
        answer=max(answer, visited.count(True))
        for i, (need, use) in enumerate(dungeons):
            if not visited[i] and need<=power:
                visited[i]=True
                dfs(power-use)
                visited[i]=False
    dfs(k)
    return answer