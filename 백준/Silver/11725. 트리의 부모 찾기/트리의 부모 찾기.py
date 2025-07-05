from collections import deque

n = int(input())

d = {i: set() for i in range(1, n + 1)}
for _ in range(n - 1):
    x, y = map(int, input().split())
    d[x].add(y)
    d[y].add(x)

relation = {}


def dfs(graph, parent, visited=set()):
    stack = deque()
    stack.append(parent)
    while stack:
        v = stack.pop()
        visited.add(v)
        for child in graph[v]:
            if child not in visited:
                relation[child] = v
                stack.append(child)


dfs(d, 1)
for i in range(2, n + 1):
    print(relation[i])
