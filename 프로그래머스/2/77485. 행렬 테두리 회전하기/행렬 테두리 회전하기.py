def solution(rows, columns, queries):
    answer = []
    grid = []
    for i in range(rows):
        start = i*columns+1
        new = [v for v in range(start, start+columns)]
        grid.append(new)
    
    for query in queries:
        r1, c1, r2, c2 = [x-1 for x in query]
        new_grid = [row[:] for row in grid]
        temp = []
        for c in range(c1+1, c2+1): # 오른쪽
            new_grid[r1][c] = grid[r1][c-1]
            temp.append(grid[r1][c-1])
        for r in range(r1+1, r2+1): # 아래
            new_grid[r][c2] = grid[r-1][c2]
            temp.append(grid[r-1][c2]) # 왼쪽
        for c in range(c1, c2):
            new_grid[r2][c] = grid[r2][c+1]
            temp.append(grid[r2][c+1])
        for r in range(r1, r2): # 위
            new_grid[r][c1] = grid[r+1][c1]
            temp.append(grid[r+1][c1])
        grid = new_grid
        answer.append(min(temp))
        
    return answer

# r1,c1부터 r2,c2까지 회전
# r, c+1: r1의 c1~c2-1
# r+1, c: c2의 r1~r2-1
# r, c-1: r2의 c1+1~c2
# r-1, c: c1의 r1+1~r2