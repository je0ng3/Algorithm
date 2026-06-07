def is_valid(s):
    stack = []
    match = {
        '(':')', ')':'(',
        '[':']', ']':'[',
        '{':'}', '}':'{'
    }
    
    for c in s:
        if c in '([{':
            stack.append(c)
        else:
            if not stack:
                return False
            if stack[-1] != match[c]:
                return False
            stack.pop()
    return not stack


def solution(s):
    answer = 0     
    for i in range(len(s)):
        if is_valid(s[i:]+s[:i]):
            answer += 1
    return answer