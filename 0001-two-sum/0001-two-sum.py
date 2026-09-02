class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i, num in enumerate(nums):
            maps[num] = i
        for i, num in enumerate(nums):
            if target-num in maps and maps[target-num]!=i:
                return [maps[target-num], i]
        return -1