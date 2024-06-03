import math

def solution(n):
    arr = [1 for i in range(n+1)]
    for i in range(2, int(math.sqrt(n))+1):
        if arr[i]:
            j = 2
            while i*j<=n:
                arr[i*j]=0
                j+=1
    _arr = [i for i in arr if i==1]
    answer = len(_arr)-2
    return answer