class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        nums = list(map(str, nums))
        while i<len(nums):
            for j in range(i):
                if nums[j]+nums[i]<nums[i]+nums[j]:
                    tmp = nums[i]
                    del nums[i]
                    nums.insert(j, tmp)
                    break
            i+=1
        return str(int(''.join(nums)))