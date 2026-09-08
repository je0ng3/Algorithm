def solution(sequence, k):
    answer = [0, len(sequence)-1]
    left, total = 0, 0
    for right in range(len(sequence)):
        total += sequence[right]
        while total>k:
            total -= sequence[left]
            left += 1
        if total==k and right-left<answer[1]-answer[0]:
            answer = [left, right]
    return answer