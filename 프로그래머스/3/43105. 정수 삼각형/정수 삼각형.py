def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j==0:
                c = 0
            elif j==len(triangle[i])-1:
                c = j-1
            else:
                c = j if triangle[i-1][j-1]<triangle[i-1][j] else j-1
            triangle[i][j] += triangle[i-1][c]
    answer = max(triangle[-1])
    return answer
