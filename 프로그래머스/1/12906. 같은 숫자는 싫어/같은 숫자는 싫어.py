def solution(arr):
    answer = []
    index = 0
    for i in arr:
        if index>0 and answer[index-1]==i:
            continue
        else:
            answer.append(i)
            index+=1
    return answer