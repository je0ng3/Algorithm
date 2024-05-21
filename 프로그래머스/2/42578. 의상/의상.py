def solution(clothes):
    set = {}
    for [a, b] in clothes:
        if b in set:
            set[b]+=1
        else:
            set[b] = 1
    answer = 1
    for i in set.values():
        answer *= (i+1)
        
    return answer-1