def solution(a, b, c):
    answer = 0
    if (a!=b and b!=c and a!=c):
        answer+= (a+b+c)
    elif (a==b and b==c):
        answer+= ((a+b+c)*(a*a+b*b+c*c)*(a**3+b**3+c**3))
    else:
        answer+=((a+b+c)*(a*a+b*b+c*c))
    return answer