class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(parent, x):
            if parent[x]!=x:
                parent[x] = find(parent, parent[x])
            return parent[x]
        
        def union(parent, a, b):
            root_a = find(parent, a)
            root_b = find(parent, b)
            if root_a<root_b:
                parent[root_b] = root_a
            else:
                parent[root_a] = root_b

        n = len(isConnected)
        parent = [i for i in range(n)]
        for i in range(n):
            for j in range(i+1, n): # 대칭 행렬이라 반만 확인
                if isConnected[i][j]==1:
                    union(parent, i, j)
        
        root = [find(parent, i) for i in range(n)]
        return len(set(root))