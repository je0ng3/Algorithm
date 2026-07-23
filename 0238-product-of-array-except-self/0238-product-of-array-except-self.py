class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        temp = 1
        for num in nums:
            answer.append(temp)
            temp*=num
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i]*=temp
            temp*=nums[i]
        return answer