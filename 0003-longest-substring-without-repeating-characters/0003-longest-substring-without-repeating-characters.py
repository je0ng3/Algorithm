class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = left = 0
        used = {}
        for i, c in enumerate(s):
            if c in used and used[c]>=left:
                left = used[c]+1
            used[c] = i
            answer = max(answer, i-left+1)
        return answer