def solution(board, moves):
    answer = 0
    stack = [0]
    n = len(board[0])
    c = [[] for _ in range(n)]
    for i in range(n):
        c[i] = [j[i] for j in board[::-1] if j[i]!=0]
    for move in moves:
        if len(c[move-1])>0:
            pick = c[move-1].pop()
            if stack[-1] == pick:
                answer+=2
                stack.pop()
            else:
                stack.append(pick)
    return answer
