class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, (x, y) in enumerate(points):
            distance = x**2 + y**2
            heapq.heappush(heap, (distance, i))
        answer = []
        for _ in range(k):
            d, i = heapq.heappop(heap)
            answer.append(points[i])
        return answer