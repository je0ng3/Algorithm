def solution(land):
    n = len(land)
    dp = [[0]*4 for _ in range(n-1)]
    last_l = land[0]
    for r, l in enumerate(land[1:]):
        sorted_l=sorted(last_l, reverse=True)
        max_idx = last_l.index(sorted_l[0])
        for c in range(4):
            if c==max_idx:
                dp[r][c] = l[c]+sorted_l[1]
            else:
                dp[r][c] = l[c]+sorted_l[0]
        last_l = dp[r]
    answer = max(dp[-1])
    return answer


# 10 11 12 11
# 16 15 13 13