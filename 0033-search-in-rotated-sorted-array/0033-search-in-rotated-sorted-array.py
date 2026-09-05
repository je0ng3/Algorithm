class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = nums.index(min(nums))
        left = nums[:pivot]
        right = nums[pivot:]
        if target in set(left):
            return left.index(target)
        if target in set(right):
            return pivot+right.index(target)
        return -1