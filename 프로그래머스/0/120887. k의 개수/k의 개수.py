def solution(i, j, k):
    answer = 0
    for n in range(i,j+1):
        answer+=list(str(n)).count(str(k))
    return answer