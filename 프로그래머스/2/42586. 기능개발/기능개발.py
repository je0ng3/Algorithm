def solution(progresses, speeds):
    left = [
        (100 - i) // j + (1 if (100 - i) % j != 0 else 0)
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
