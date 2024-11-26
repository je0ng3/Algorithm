def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        a = numLog[i+1]-numLog[i]
        if a == 1:
            answer+='w'
        elif a==-1:
            answer+='s'
        elif a==10:
            answer+='d'
        else:
            answer+='a'
    return answer