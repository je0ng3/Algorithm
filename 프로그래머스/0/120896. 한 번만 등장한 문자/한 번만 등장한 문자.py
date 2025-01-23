def solution(s):
    a = []
    for i in list(s):
        if s.count(i)==1:
            a.append(i)
    a.sort()
    return ''.join(a)