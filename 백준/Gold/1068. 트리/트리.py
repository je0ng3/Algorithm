n = int(input())
parents = list(map(int, input().split()))

tree = {i: set() for i in range(n)}
for child, parent in enumerate(parents):
    if parent == -1:
        continue
    tree[parent].add(child)


def dfs(graph, start, visited=set()):
    visited.add(start)
    for child in graph[start]:
        if child not in visited:
            dfs(graph, child, visited)
    del graph[start]


delete = int(input())
dfs(tree, delete)
count = 0
for node in tree:
    if len(tree[node]) == 0:
        count += 1
    elif delete in tree[node] and len(tree[node]) == 1:
        count += 1
print(count)
