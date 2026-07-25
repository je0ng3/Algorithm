def solution(n):
    answer = 0
    queens = [-1]*n
    def is_valid(row, col):
        for r in range(row):
            c = queens[r]
            if c==col:
                return False
            if abs(row-r)==abs(col-c):
                return False
        return True
    
    def dfs(row):
        nonlocal answer
        if row==n:
            answer += 1
            return
        for col in range(n):
            if is_valid(row, col):
                queens[row]=col
                dfs(row+1)
                queens[row]=-1
    
    dfs(0)
    return answer