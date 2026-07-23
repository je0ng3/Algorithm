class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(lst, t):
            l,r=0,len(lst)
            while l<=r:
                mid = (l+r)//2
                if lst[mid]<t:
                    l=mid+1
                elif lst[mid]>t:
                    r=mid-1
                else:
                    return mid
            return -1

        if not nums or target not in set(nums):
            return -1
        answer = 0
        # 정렬된 두 리스트로 분리
        left = right = 0
        while right<len(nums) and nums[left]<=nums[right]:
            right+=1
        # target이 속한 리스트 찾기
        # 1. left~right-1
        # 2. right~len(nums)-1
        if nums[left]<=target<=nums[right-1]:
            idx = binary_search(nums[left:right], target)
            return idx
        else:
            idx = binary_search(nums[right:len(nums)], target)
            if idx==-1:
                return idx
            else:
                return right+idx