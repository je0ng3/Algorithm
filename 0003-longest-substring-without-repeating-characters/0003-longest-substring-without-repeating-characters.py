class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start, maxi = 0, 0
        for i, c in enumerate(s):
            if c in used:
                start = max(start,used[c]+1)
            used[c]=i
            maxi = max(maxi, i-start+1)
        return maxi