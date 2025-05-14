def solution(progresses, speeds):
    left = [
        -((i-100) // j )
        for i, j in zip(progresses, speeds)
    ]
    temp = [0]
    answer = []
    for i in left:
        if i > temp[-1]:
            temp.append(i)
            answer.append(1)
        else:
            answer[-1]+=1
    return answer
