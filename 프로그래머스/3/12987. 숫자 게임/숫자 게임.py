def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    n = len(A)
    i, j = 0, 0 
    while i<n and j<n:
        if A[i]<B[j]:
            answer += 1
            i += 1
            j += 1
        else:
            j += 1
    return answer

 