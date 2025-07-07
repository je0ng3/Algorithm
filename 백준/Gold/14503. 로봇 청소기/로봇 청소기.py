n, m = map(int, input().split())
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

count = 0
while True:
    if room[r][c] == 0:
        room[r][c] = -1
        count += 1
    else:
        r -= dx[d]
        c -= dy[d]
        if not (0 < r < n and 0 < c < m):
            break
        if room[r][c] == 1:
            break
    exist = False
    for i in range(1, 5):
        head = (d - i) % 4
        nx = r + dx[head]
        ny = c + dy[head]
        if room[nx][ny] == 0:
            r, c = nx, ny
            d = head
            break

print(count)
