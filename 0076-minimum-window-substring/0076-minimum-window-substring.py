class Solution:
    def minWindow(self, s: str, t: str) -> str:
        answer = ''
        size = float('inf')

        mine = collections.Counter()
        t_counts = collections.Counter(t)

        left = 0
        for right in range(len(s)):
            # 확장 
            mine[s[right]] += 1
            # 모든 t 포함
            while all(mine[c] >= t_counts[c] for c in t_counts):
                if right-left+1<size:
                    size=right-left+1
                    answer = s[left:right+1]
                # 축소
                mine[s[left]]-=1
                left+=1
        return answer