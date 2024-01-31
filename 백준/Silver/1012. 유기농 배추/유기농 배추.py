import sys

t = int(input())
for _ in range(t):
  m, n, k = map(int, sys.stdin.readline().split())
  field = [[0 for i in range(n)] for j in range(m)]
  for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    field[x][y] = 1
  count = 0
  for i in range(m):
    for j in range(n):
        if field[i][j] == 1:
            count += 1
            stack = [(i, j)]
            field[i][j] = 0 
            while stack:
                x, y = stack.pop()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and field[nx][ny] == 1:
                        stack.append((nx, ny))
                        field[nx][ny] = 0  

  print(count)


          
  
  