from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        q = deque()
        for i, t in enumerate(temperatures):
            while q and temperatures[q[-1]]<t:
                idx = q.pop()
                answer[idx] = i-idx
            q.append(i)
        return answer