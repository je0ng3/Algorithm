def solution(clothes):
    answer = 1
    dic = {}
    for c, t in clothes:
        h = hash(t)
        if h not in dic:
            dic[h] = 2  # t 타입의 옷이 없는 경우 + 있는 경우 = 2
        else:
            dic[h] += 1
    for v in dic.values():
        answer *= v
    return answer -1 # 아무것도 착용하지 않는 경우 1