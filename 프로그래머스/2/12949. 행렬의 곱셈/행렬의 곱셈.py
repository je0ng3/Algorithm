def solution(arr1, arr2):
    a=len(arr1)
    b=len(arr2)
    c=len(arr2[0])
    
    answer = [[0]*c for _ in range(a)]
    for r_ in range(a):
        for c_ in range(c):
            for b_ in range(b):
                answer[r_][c_] += arr1[r_][b_]*arr2[b_][c_]
    
    return answer


# arr1: a x b
# arr2: b x c
# arr1 x arr2: a x c

