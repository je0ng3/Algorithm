from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 윈도우 내 출현 빈도가 가장 높은 문자의 수를 뺀 값이 k와 같을 수 있는 수 중 가장 큰 최댓값
        left = right = 0
        counts = Counter()
        for right in range(1, len(s)+1):
            counts[s[right-1]]+=1
            max_char_n = counts.most_common(1)[0][1]
            if right-left-max_char_n>k:
                counts[s[left]]-=1
                left +=1
        return right-left