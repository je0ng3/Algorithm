import copy

def solution(m, n, board):
    answer = 0
    remove = 1
    board = [list(b) for b in board]
    while remove > 0:
        remove, board = check(board, m, n)
        answer += remove
        board = move(board, m, n)
    return answer

# 4블록을 이루는 모든 블록 체크 -> 사라질 블록 개수, 체크된 보드
def check(board, m, n):
    check_board = copy.deepcopy(board)
    for y in range(m-1):
        for x in range(n-1):
            if board[y][x]!=-1 and board[y][x]==board[y+1][x]==board[y][x+1]==board[y+1][x+1]:
                check_board[y][x]=check_board[y+1][x]=check_board[y][x+1]=check_board[y+1][x+1]=0
    count = [b.count(0) for b in check_board]
    return (sum(count), check_board)

# 없어진 블록에 따라 떨어질 블록 이동 -> 이동한 보드 
def move(board, m, n):
    move_board = [[0]*n for _ in range(m)]
    for x in range(n):
        temp = []
        for y in range(m):
            if board[y][x]!=0 and board[y][x]!=-1:
                temp.append(board[y][x])
        temp = [-1 for _ in range(m-len(temp))] + temp
        for y in range(m):
            move_board[y][x] = temp.pop(0)
    return move_board