def solution(n, lost, reserve):
    answer = n
    s1 = set(lost)
    s2 = set(reserve)
    s3 = s1-s2 # 체육복 없는 학생
    s4 = s2-s1 # 여분 체육복 있는 학생
    for i in sorted(s3):
        if i-1 in s4:
            s4.remove(i-1)
        elif i+1 in s4:
            s4.remove(i+1)
        else:
            answer-=1
    return answer