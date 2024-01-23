def solution(n):
    i = 0
    for i in range(1, n+1):
        if i*i == n:
            return (i+1)*(i+1)
        elif i*i > n:
            break
    return -1