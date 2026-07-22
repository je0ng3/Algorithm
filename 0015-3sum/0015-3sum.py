class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            num=nums[i]
            if num>0:
                break
            if i>0 and num==nums[i-1]:
                continue
            j,k =i+1, n-1
            while j<k:
                s = nums[j]+nums[k]+num
                if s>0:
                    k-=1
                elif s<0:
                    j+=1
                else:
                    answer.append([num, nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return answer