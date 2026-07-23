class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        
        idx = -1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                idx = mid
                break
        if idx==-1:
            return [-1, -1]
        left=right=idx
        while left>=0 and nums[left]==target:
            left-=1
        while right<len(nums) and nums[right]==target:
            right+=1
        return [left+1, right-1]
        