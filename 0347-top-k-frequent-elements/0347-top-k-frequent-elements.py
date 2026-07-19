class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        heap = []
        for count in counts:
            heapq.heappush(heap, (-counts[count], count))
        answer = []
        for _ in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer