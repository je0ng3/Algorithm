class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter_s = [c for c in s.lower() if c.isalnum()]
        return filter_s==filter_s[::-1]