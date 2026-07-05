def solution(n, s):
    if n>s:
        return [-1]
    answer = [s//n]*n
    for i in range(s%n):
        answer[n-i-1]+=1
    return answer

# n개의 자연수로 s만들기
# 각 원소의 곱이 최대 -> n개의 자연수의 평균이 최대 
# -> s를 n 개로 균등히 나누고, 나머지는 하나씩 분배

