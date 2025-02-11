def solution(n, k):
    answer = 0
    k = max(0, k-(n//10))
    answer = 12000*n + 2000*k
    return answer