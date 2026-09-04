from collections import Counter, deque
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counts, seen, stack = Counter(s), set(), deque()
        for c in s:
            counts[c]-=1
            if c in seen:
                continue
            # c가 stack에 담긴 것들보다 앞에 오는게 사전순으로 빠른 경우
            while stack and c<stack[-1] and counts[stack[-1]]>0:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
        return ''.join(stack)