def solution(array, n):
    a =[]
    for i in array:
        a.append((abs(i-n),i))
    a.sort()
    return a[0][1]