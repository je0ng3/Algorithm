def solution(x):
    digitSum = sum(list(map(int,list(str(x)))))
    if x%digitSum == 0:
        return True
    else:
        return False
