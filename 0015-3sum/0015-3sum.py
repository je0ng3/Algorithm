class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if 0<i and nums[i]==nums[i-1]:
                continue
            target = nums[i]
            left, right = i+1, n-1
            while left<right:
                sum3 = target+nums[left]+nums[right]
                if sum3==0:
                    answer.append([nums[i], nums[left], nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left +=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif sum3<0:
                    left +=1
                elif sum3>0:
                    right -=1
        return answer