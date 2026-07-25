from collections import defaultdict
import heapq

def solution(N, road, K):
    answer = 0
    graph = defaultdict(list)
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))
    dist = [0]+[float('inf')]*N
    dist[1] = 0 # 1번에서 시작
    heap = [(0,1)] # 시간, 마을
    while heap:
        time, node = heapq.heappop(heap)
        for nxt, t in graph[node]:
            new_time = time+t
            if new_time<=K and new_time<dist[nxt]:
                dist[nxt] = new_time
                heapq.heappush(heap, (new_time, nxt))
    for d in dist[1:]:
        if d<=K:
            answer += 1
    return answer

# n개의 마을 : 1~n
# 양방향 통행 도로
# 1번과 연결된 k 시간 이하의 마을
