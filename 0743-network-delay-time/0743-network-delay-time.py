class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if n<k:
            return -1
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))
        dist = [float('inf')]*(n+1)
        dist[k] = 0
        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)
            if time>dist[node]: # 최단거리만 계산
                continue 
            for nxt_node, w in graph[node]:
                nxt_time = time+w
                if nxt_time<dist[nxt_node]:
                    dist[nxt_node]=nxt_time
                    heapq.heappush(heap, (nxt_time, nxt_node))
        answer = max(dist[1:])
        if answer==float('inf'):
            return -1
        return answer