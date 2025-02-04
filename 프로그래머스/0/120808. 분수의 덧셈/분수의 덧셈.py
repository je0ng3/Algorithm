def solution(numer1, denom1, numer2, denom2):
    n = (numer1*denom2)+(numer2*denom1)
    d = denom1*denom2
    for i in range(min(n, d)+1, 1, -1):
        if n%i==0 and d%i==0:
            n//=i
            d//=i
    answer = [n, d]
    return answer