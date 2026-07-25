def solution(k, dungeons):
    answer = 0
    visited = [False]*len(dungeons)
    def dfs(power, cnt):
        nonlocal answer
        answer = max(answer, cnt)
        for i in range(len(dungeons)):
            if visited[i]:
                continue
            need, use = dungeons[i]
            if need<=power:
                visited[i]=True
                dfs(power-use, cnt+1)
                visited[i]=False
    dfs(k, 0)
    return answer