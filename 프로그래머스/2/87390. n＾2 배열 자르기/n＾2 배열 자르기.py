def solution(n, left, right):
    answer = []
    for idx in range(left, right+1):
        r = idx//n
        c = idx%n
        answer.append(max(r,c)+1)
    return answer

# arr[i][j] = max(i, j)+1
# r = idx//n, c = idx%n