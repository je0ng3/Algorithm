class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        stack = collections.deque()
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<t:
                a = stack.pop()
                answer[a] = i-a
            stack.append(i)
        return answer