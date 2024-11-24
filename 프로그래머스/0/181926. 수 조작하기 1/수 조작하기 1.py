def solution(n, control):
    answer = n 
    answer += control.count('w')
    answer-=control.count('s')
    answer+=(10*control.count('d'))
    answer-=(10*control.count('a'))
    return answer