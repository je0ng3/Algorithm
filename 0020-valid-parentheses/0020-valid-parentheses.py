class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        brackets = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if len(stack)==0:
                    return False
                check = stack.pop()
                if brackets[check]!=c:
                    return False
        return True if len(stack)==0 else False