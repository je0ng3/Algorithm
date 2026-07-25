def solution(rows, columns, queries):
    answer = []
    maps = [[i for i in range(columns*j+1, columns*(j+1)+1)] \
                                    for j in range(rows)]
    for query in queries:
        r1, c1, r2, c2 = [x-1 for x in query]
        used = []
        temp = [row[:] for row in maps]
        for c in range(c1+1, c2+1):
            maps[r1][c] = temp[r1][c-1]
            used.append(temp[r1][c-1])
        for c in range(c1, c2):
            maps[r2][c] = temp[r2][c+1]
            used.append(temp[r2][c+1])
        for r in range(r1, r2):
            maps[r][c1] = temp[r+1][c1]
            used.append(temp[r+1][c1])
        for r in range(r1+1, r2+1):
            maps[r][c2] = temp[r-1][c2]
            used.append(temp[r-1][c2])
        answer.append(min(used))
    return answer


# r1,c1 ~ r2,c2
# r1 | c1+1~c2 = c-1
# r2 | c1~c2-1 = c+1
# c1 | r1~r2-1 = r+1
# c2 | r1+1~r2 = r-1