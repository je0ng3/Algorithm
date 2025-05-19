def solution(n, lost, reserve):
    cant = 0
    a = list(set(reserve)-set(lost))
    b = list(set(lost)-set(reserve))
    for i in range(1, n+1):
        if i in b:
            if i-1 in a:
                continue
            elif i+1 in a:
                a.remove(i+1)
            else:
                cant+=1
    return n-cant