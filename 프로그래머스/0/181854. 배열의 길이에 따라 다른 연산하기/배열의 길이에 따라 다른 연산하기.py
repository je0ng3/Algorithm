def solution(arr, n):
    answer = []
    if len(arr)%2!=0:
        for i, j in enumerate (arr):
            if i%2==0:
                answer.append(j+n)
            else:
                answer.append(j)
    else:
        for i, j in enumerate (arr):
            if i%2!=0:
                answer.append(j+n)
            else:
                answer.append(j)
    return answer