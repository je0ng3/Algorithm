def solution(strArr):
    answer = 0
    dic = {}
    for i in strArr:
        if len(i) in dic:
            dic[len(i)] += 1
        else:
            dic[len(i)] = 1
    for key, value in dic.items():
        if value>answer:
            answer = value
    return answer