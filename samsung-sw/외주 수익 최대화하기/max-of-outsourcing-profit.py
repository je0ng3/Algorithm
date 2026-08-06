from collections import deque

n = int(input()) # 휴가 기간
jobs = [list(map(int, input().split())) for _ in range(n)] # 기한, 수익

answer = 0
def dfs(day, money):
    global answer
    if day>=n:
        answer = max(answer, money)
        return 
    t, p = jobs[day]
    if day+t<=n:
        dfs(day+t, money+p)
    dfs(day+1, money)

dfs(0, 0)
print(answer)