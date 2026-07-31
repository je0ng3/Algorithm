def solution(n, times):
    answer = 0
    left, right = 0, max(times)*n
    while left<=right:
        mid = (left+right)//2
        count = sum(mid//t for t in times)
        if count>=n:
            answer = mid
            right = mid-1
        else:
            left = mid+1
    return answer