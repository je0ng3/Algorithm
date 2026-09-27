import collections

def solution(sales, links):
    tree = collections.defaultdict(list)
    for a, b in links:
        tree[a - 1].append(b - 1)

    dp = [[0, 0] for _ in sales] # 미참, 참가
    def dfs(u):
        dp[u][1] = sales[u]
        min_extra = float('inf')

        for v in tree[u]:
            dfs(v)
            minimum = min(dp[v][0], dp[v][1])
            dp[u][1] += minimum
            dp[u][0] += minimum
            extra = dp[v][1] - minimum
            min_extra = min(min_extra, extra)

        if tree[u]:
            dp[u][0] += min_extra

    dfs(0)
    return min(dp[0])