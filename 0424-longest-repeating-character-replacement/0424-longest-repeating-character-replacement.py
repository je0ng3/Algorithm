from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 윈도우 내 출현 빈도가 가장 높은 문자의 수를 뺀 값이 k와 같을 수 있는 수 중 가장 큰 최댓값
        left = 0
        counts = Counter()
        max_char_n = 0
        for right, c in enumerate(s):
            counts[c] += 1
            max_char_n = max(max_char_n, counts[c])
            if right-left+1 -max_char_n > k:
                counts[s[left]]-=1
                left +=1
        return right-left+1