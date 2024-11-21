import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
a = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
d = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            d[i][j] = a[i][j]
        elif i == 0:
            d[i][j] = a[i][j] + d[i][j - 1]
        elif j == 0:
            d[i][j] = a[i][j] + d[i - 1][j]
        else:
            d[i][j] = d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1] + a[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    if x1 == 1 and y1 == 1:
        print(d[x2 - 1][y2 - 1])
    elif x1 == 1:
        print(d[x2 - 1][y2 - 1] - d[x2 - 1][y1 - 2])
    elif y1 == 1:
        print(d[x2 - 1][y2 - 1] - d[x1 - 2][y2 - 1])
    else:
        print(
            d[x2 - 1][y2 - 1]
            - d[x1 - 2][y2 - 1]
            - d[x2 - 1][y1 - 2]
            + d[x1 - 2][y1 - 2]
        )
