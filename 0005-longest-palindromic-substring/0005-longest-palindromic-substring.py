class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrom(left, right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1    
            return s[left+1:right]
        
        answer = ''
        for i in range(len(s)):
            a = is_palindrom(i, i)
            b = is_palindrom(i, i+1)
            if len(a)>len(answer):
                answer = a
            if len(b)>len(answer):
                answer = b
        return answer