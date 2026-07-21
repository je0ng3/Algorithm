class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = nums[0]
        for num in nums[1:]:
            answer ^= num # answer = 0 if answer==num else num 
        return answer