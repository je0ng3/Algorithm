class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        nums.sort()
        for i, n in enumerate(nums[:-2]):
            if n>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                left, right = nums[l], nums[r]
                s = left+right+n
                if s==0:
                    answer.append([n, left, right])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif s<0:
                    l+=1
                else:
                    r-=1
        return answer