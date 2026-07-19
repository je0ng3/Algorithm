class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counters = collections.Counter(s)
        seen = set()
        stack = collections.deque()

        for c in s:
            counters[c]-=1
            if c in seen:
                continue

            while stack and c < stack[-1] and counters[stack[-1]]>0:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)

        return ''.join(stack)