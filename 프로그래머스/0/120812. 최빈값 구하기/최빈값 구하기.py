def solution(array):
    a = set(array)
    answer = 0
    b = 0
    c = 0
    for i in list(a):
        if array.count(i)>b:
            answer = i
            b = array.count(i)
            c = 0
        elif array.count(i)==b:
            c = 1
    if c:
        answer = -1
    return answer