from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())

    q = deque()
    q.append("1")
    while True:
        x = q.popleft()
        val = int(x)
        if val % n == 0:
            print(x)
            break
        q.append(x+"0")
        q.append(x+"1")