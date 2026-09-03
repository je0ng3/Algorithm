class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        p = 1
        for i in range(len(nums)):
            answer.append(p)
            p*=nums[i]
        p = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            answer[i]*=p
            p*=nums[i]
        return answer