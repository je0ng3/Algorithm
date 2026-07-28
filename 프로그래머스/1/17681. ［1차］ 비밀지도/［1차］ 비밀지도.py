def solution(n, arr1, arr2):
    binary = []
    for a in arr1:
        a = bin(a)[2:]
        a = ['0']*(n-len(a))+list(a)
        binary.append(a)
    for i, b in enumerate(arr2):
        b = list(bin(b)[2:])
        b = ['0']*(n-len(b))+list(b)
        binary[i] = list(int(a_) or int(b_) for a_, b_ in zip(binary[i], b))
    answer = []
    for row in range(n):
        temp = ''
        for col in range(n):
            if binary[row][col]:
                temp+='#'
            else:
                temp+=' '
        answer.append(temp)
    return answer