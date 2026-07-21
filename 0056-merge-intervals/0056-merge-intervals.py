class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        intervals.sort(key=lambda x: (x[0], x[1]))
        q = collections.deque(intervals)
        s, e = q.popleft()
        while q:
            a, b = q.popleft()
            if a<=e:
                e=max(e,b)
            else:
                answer.append([s,e])
                s, e = a, max(e,b)
        answer.append([s,e])
        return answer