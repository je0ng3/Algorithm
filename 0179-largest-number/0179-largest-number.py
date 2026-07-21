class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        i_sort = []
        for num in nums:
            check = 0
            for i, cur in enumerate(i_sort):
                if cur+num < num+cur:
                    i_sort = i_sort[:i]+[num]+i_sort[i:]
                    check = 1
                    break
            if check:
                continue
            i_sort.append(num)
        return str(int(''.join(i_sort)))