def solution(n, computers):
    answer = 0
    parent = [i for i in range(n)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra != rb:
            parent[rb] = ra
    
    for r in range(n):
        for c in range(n):
            if r==c:
                continue
            if computers[r][c]==1:
                union(r,c)
    
    roots = set(find(i) for i in range(n))
    answer = len(roots)
    return answer