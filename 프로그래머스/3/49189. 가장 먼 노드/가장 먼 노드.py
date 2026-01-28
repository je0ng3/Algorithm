from collections import deque

def solution(n, edge):
    answer = 0    
    graph = {i:[] for i in range(1, n+1)}
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    distance = [-1]*(n+1)
    distance[1] = 0

    queue = deque([1])
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if distance[nxt]==-1:
                distance[nxt] = distance[cur]+1
                queue.append(nxt)
    max_dist = max(distance)
    answer = distance.count(max_dist)
    return answer