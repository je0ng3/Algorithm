from collections import Counter

def solution(k, tangerine):
    answer = 0
    counts = sorted(Counter(tangerine).values(), reverse=True) # 개수 내림차순
    
    total = 0
    for i, cnt in enumerate(counts, 1):
        total += cnt
        if total >= k:
            return i
    
    return answer