def solution(a, b):
    return max(a*pow(10,len(str(b)))+b, b*pow(10,len(str(a)))+a)