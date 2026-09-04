from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False

        dic = {
            '(':')', 
            '{':'}',
            '[':']'
        }
        stack = deque()
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if not stack or dic[stack.pop()]!=c:
                    return False
        return len(stack)==0