class NumArray:

    def __init__(self, nums: List[int]):
        prefix_sums = [0]
        cur = 0
        for num in nums:
            cur += num
            prefix_sums.append(cur)
        self.ps = prefix_sums

    def sumRange(self, left: int, right: int) -> int:
        return self.ps[right+1]-self.ps[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)