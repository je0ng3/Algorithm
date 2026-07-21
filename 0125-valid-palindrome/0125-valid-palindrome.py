class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = [c.lower() for c in s if c.isalnum()]
        return strs == strs[::-1]