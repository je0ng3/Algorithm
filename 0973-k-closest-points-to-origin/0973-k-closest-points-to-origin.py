class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = x**2 + y**2
            heapq.heappush(heap, (distance, x, y))
        answer = []
        for _ in range(k):
            d, x, y = heapq.heappop(heap)
            answer.append([x, y])
        return answer