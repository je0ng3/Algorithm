def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if (i+1)%2==0:
            answer.append(strArr[i].upper())
        else:
            answer.append(strArr[i].lower())
    return answer