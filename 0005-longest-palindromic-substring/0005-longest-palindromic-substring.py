class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrom(left, right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1    
            return s[left+1:right]
        
        if s==s[::-1]:
            return s

        answer = ''
        for i in range(len(s)):
            a = is_palindrom(i, i)
            b = is_palindrom(i, i+1)
            answer = max(answer, a, b, key=len)
        return answer