class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]>nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left

        if target>=nums[0]: 
            left, right = 0, pivot-1
            if right==-1:
                right = len(nums)-1
        else:
            left, right = pivot, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]>target:
                right = mid-1
            elif nums[mid]<target:
                left = mid+1
            else:
                return mid
        return -1