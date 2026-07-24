from collections import defaultdict, deque

def solution(N, road, K):
    answer = 0
    graph = defaultdict(list)
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))
    dist = [0]+[float('inf')]*N
    dist[1] = 0 # 1번에서 시작
    q = deque([(1, 0)]) # 마을, 도달시간
    while q:
        node, time = q.popleft()
        if time==K:
            continue
        for nxt, t in graph[node]:
            new_time = time+t
            if new_time<=K and new_time<dist[nxt]:
                dist[nxt] = new_time
                q.append((nxt, new_time))
    for d in dist[1:]:
        if d<=K:
            answer += 1
    return answer

# n개의 마을 : 1~n
# 양방향 통행 도로
# 1번과 연결된 k 시간 이하의 마을
