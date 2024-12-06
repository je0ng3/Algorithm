def solution(a, d, included):
    answer = 0
    num = a
    for i in included:
        if i:
            answer+= num
        num+=d
    return answer