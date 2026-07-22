class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        q = collections.deque()
        for i, num in enumerate(nums):
            # num보다 작은 수는 num이 포함된 윈도우에서 최대가 될 수 없음
            while q:
                idx = q.pop()
                n = nums[idx]
                if n>num:
                    q.append(idx)
                    break

            # 윈도우에 num 인덱스 추가 
            q.append(i)

            # 윈도우 크기 벗어나면 맨 앞 제거
            if i>=k and i-q[0]+1>k:
                 q.popleft()
            
            # 윈도우 꽉 채웠을 때, 최대 슬라이싱 윈도우 값 추가
            if i+1>=k:
                answer.append(nums[q[0]])
        return answer