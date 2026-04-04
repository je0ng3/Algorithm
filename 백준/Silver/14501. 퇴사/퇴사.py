n = int(input())    # 상담 일수 

t = [0]*n  # 상담 기간
p = [0]*n  # 수익
for i in range(n):
    t[i], p[i] = map(int, input().split())   

dp = [0]*(n+1) 
for i in range(n-1, -1, -1):
    if i+t[i]<=n: 
        dp[i] = max(dp[i+1], p[i]+dp[i+t[i]])
    else:
        dp[i] = dp[i+1]

print(dp[0])