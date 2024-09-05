def solution(n):
    answer = 0
    temp = []
    while n:
        temp.append(n%3)
        n//=3
    temp.reverse()
    t = 1
    for i in temp:
        answer+= (i*t)
        t*=3
    return answer