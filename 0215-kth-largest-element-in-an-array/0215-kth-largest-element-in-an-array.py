class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        big_k = []
        for _ in range(k):
            big_k.append(heapq.heappop(heap))
        return -big_k[-1]