def solution(participant, completion):
    answer = ''
    dic = {}
    temp = 0
    for p in participant:
        dic[hash(p)] = p
        temp += int(hash(p))
    for c in completion:
        temp -= hash(c)
    answer = dic[temp]
    return answer