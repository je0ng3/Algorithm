class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        heap = []
        for k, v in counts.items():
            heapq.heappush(heap, (0, -v, k))
        now = 1
        can_work = []
        while heap or can_work:
            # now<=idle인 작업 중 count가 가장 큰 값 
            while heap:
                idle, count, task = heapq.heappop(heap) 
                if idle<=now:
                    heapq.heappush(can_work, (count, task))
                else:
                    heapq.heappush(heap, (idle, count, task))
                    break
            if can_work:
                count, task = heapq.heappop(can_work)
            else:
                idle, count, task = heapq.heappop(heap)
                now = idle
            if count<-1:
                heapq.heappush(heap, (now+n+1, count+1, task))
            now += 1
        return now-1