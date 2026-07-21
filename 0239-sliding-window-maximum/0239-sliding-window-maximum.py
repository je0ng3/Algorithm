class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        q = collections.deque()
        for i, num in enumerate(nums):
            # 윈도우 내의 수 체크. 앞으로 최대값 될 수 없으면 제거 
            while q and nums[q[-1]]<=num:
                q.pop()
            # 윈도우에 현재 값 추가
            q.append(i)
            # 윈도우 크기 벗어나면 현재까지의 최대값 제거
            if q[0]<=i-k:
                q.popleft()
            # 꽉 채워진 윈도우 내에서 최대값 출력
            if i>=k-1:
                answer.append(nums[q[0]])
        return answer