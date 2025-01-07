def solution(n):
    answer = 1
    for i in range(1,11):
        answer *= i
        if n<answer:
            return i-1
        elif n==answer:
            return i
