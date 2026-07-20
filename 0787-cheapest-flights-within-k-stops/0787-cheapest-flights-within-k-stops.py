class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v,w))

        heap = [(0, src, k)]
        visited = {}

        while heap:
            price, node, stop = heapq.heappop(heap)
            if node==dst:
                return price
                
            if (node, stop) in visited:
                continue
            visited[(node, stop)] = price

            if stop>=0:
                for v, w in graph[node]:
                    nxt_price = price+w
                    heapq.heappush(heap, (nxt_price, v, stop-1))
        
        return -1