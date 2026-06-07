def solution(n,a,b):
    answer = 0
    while a!=b:
        a = (a+1)//2
        b = (b+1)//2
        answer += 1
    return answer

# 다음 라운드의 번호
# (현재번호 + 1)//2
