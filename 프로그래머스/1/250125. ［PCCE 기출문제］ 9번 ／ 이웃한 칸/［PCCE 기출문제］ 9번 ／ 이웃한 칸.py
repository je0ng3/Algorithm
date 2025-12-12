def solution(board, h, w):
    n = len(board)
    count = 0
    dh, dw = [0,1,-1,0], [1,0,0,-1]
    target = board[h][w]
    for i in range(4):
        h_check, w_check = h+dh[i], w+dw[i]
        if min(h_check, w_check)>=0 and max(h_check, w_check)<n:
            if target == board[h_check][w_check]:
                count += 1
    return count