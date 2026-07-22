class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        num_set = set(nums)
        for num in num_set:
            if num-1 in num_set: # 시작점 아니면 넘김
                continue
            leng = 1
            cur = num
            while cur+1 in num_set:
                cur+=1
                leng+=1
            answer = max(answer, leng)
        return answer