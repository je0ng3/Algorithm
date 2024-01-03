def solution(s):
    answer = ''
    s = list(s)
    up = 1
    for i in s:
        if up==1:
            answer += i.upper()
        else:
            answer += i.lower() 
        if i==' ':
            up = 1
        else:
            up = 0
    return answer
