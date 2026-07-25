import heapq
from collections import defaultdict

def solution(N, road, K):
    graph = defaultdict(list)
    for u, v, w in road:
        graph[u].append((v,w))
        graph[v].append((u, w))
        
    heap = [(0,1)] # 시간, 노드
    dist = [float('inf')]*(N+1)
    dist[1]=0
    while heap:
        time, node = heapq.heappop(heap)
        for v, w in graph[node]:
            nxt_time = time+w
            if nxt_time<=K and nxt_time<dist[v]:
                dist[v] = nxt_time
                heapq.heappush(heap, (nxt_time, v))
    answer = len([d for d in dist if d!=float('inf')])
    return answer