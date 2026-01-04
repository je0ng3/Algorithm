from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for lsts in list(permutations(dungeons)):
        temp = count = 0
        for (need, use) in lsts:
            if temp+need > k:
                continue
            temp += use
            count += 1
        answer = max(count, answer)
    return answer