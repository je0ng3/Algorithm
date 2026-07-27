def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    parent = [i for i in range(n+1)]
    
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    
    def union(a, b):
        parent_a = find(a)
        parent_b = find(b)
        if parent_a==parent_b: # 순환
            return False
        parent[parent_b]=parent_a
        return True

    for u, v, w in costs:
        if union(u, v):
            answer += w
    return answer