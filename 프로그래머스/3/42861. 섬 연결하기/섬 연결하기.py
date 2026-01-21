def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    parent = [ i for i in range(n)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False
        parent[rb] = ra
        return True
    
    for a, b, cost in costs:
        if union(a, b):
            answer+=cost
    return answer