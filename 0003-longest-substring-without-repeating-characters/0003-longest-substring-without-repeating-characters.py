class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n<=1:
            return n
        
        answer = 0
        for i in range(n-1):
            if answer>n-i:
                break
            check = set([s[i]])
            for j in range(i+1, n):
                new = s[j]
                if new in check:
                    break
                check.add(new)
            answer = max(answer, len(check))
        return answer