def solution(n):
    answer = 0
    for i in range(n+1):
        if i<4:
            continue
        for j in range(2, i):
            if i%j==0:
                answer+=1
                break
    return answer