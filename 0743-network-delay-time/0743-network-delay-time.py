class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))
        
        dist = [float('inf')]*(n+1)
        dist[k] = 0
        
        heap = [(0,k)]
        while heap:
            time, node = heapq.heappop(heap)
            if time>dist[node]:
                continue

            for nxt_node, weight in graph[node]:
                nxt_time = time+weight
                if nxt_time<dist[nxt_node]:
                    dist[nxt_node]=nxt_time
                    heapq.heappush(heap, (nxt_time, nxt_node))
        
        answer = max(dist[1:])
        return -1 if answer==float('inf') else answer