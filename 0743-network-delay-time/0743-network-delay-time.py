class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')]*(n+1)
        dist[k] = 0
        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)
            for v, w in graph[node]:
                t = time+w
                if dist[v]>t:
                    dist[v] = t
                    heapq.heappush(heap, (t, v)) 
        answer = max(dist[1:])
        if answer==float('inf'):
            return -1
        return answer       