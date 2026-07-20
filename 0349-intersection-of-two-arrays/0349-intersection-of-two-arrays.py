class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = set()
        nums1 = sorted(set(nums1))
        nums2 = sorted(set(nums2))
        i=j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                answer.add(nums1[i])
                i+=1
                j+=1
        return list(answer)