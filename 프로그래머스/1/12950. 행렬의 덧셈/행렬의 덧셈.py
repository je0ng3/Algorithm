def solution(arr1, arr2):
    rowSize = len(arr1)
    colSize = len(arr1[0])
    answer = [[0] * colSize for _ in range(rowSize)]
    for i in range(rowSize):
        for j in range(colSize):
            answer[i][j] = arr1[i][j]+arr2[i][j]
    return answer