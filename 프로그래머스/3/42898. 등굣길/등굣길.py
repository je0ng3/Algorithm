def solution(m, n, puddles):
    MOD = 1000000007
    
    dp = [[0]*m for _ in range(n)]
    dp[0][0]=1 # 0,0 에 있는 방법 1가지
    
    puddles = set(map(tuple, puddles))
    
    for r in range(n):
        for c in range(m):
            if r==0 and c==0:
                continue
            if (c+1, r+1) in puddles: # 물웅덩이 인덱스 1부터 시작
                continue
            
            up = dp[r-1][c] if r>0 else 0
            left = dp[r][c-1] if c>0 else 0
            dp[r][c] = (up+left)%MOD
    
    return dp[n-1][m-1]

# 오른쪽, 아래쪽으로만 이동 : 모든 경로가 최단
# 이동 횟수 = (m-1) + (n-1)
# dp[r][c] = dp[r-1][c] + dp[r][c-1]