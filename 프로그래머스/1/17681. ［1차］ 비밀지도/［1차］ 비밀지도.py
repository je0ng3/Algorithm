def ten2too(i):
    a = []
    while i>0:
        a.append(i%2)
        i//=2
    return a

def solution(n, arr1, arr2):
    answer = ["" for _ in range(n)]
    one = list(map(ten2too, arr1))
    two = list(map(ten2too, arr2))
    for i in range(n):
        for j in range(n-1,-1,-1):
            if (len(one[i])>j and one[i][j]==1) or (len(two[i])>j and two[i][j]==1):
                answer[i]+='#'
            else:
                answer[i]+=' '
    return answer