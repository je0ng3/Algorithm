n, m = map(int, input().split())
dic = { i: set() for i in range(1,n+1)}
for _ in range(m):
    x, y = map(int, input().split())
    dic[x].add(y)
    dic[y].add(x)

answer = 0
for i in range(1, n-1):
    for j in range(i+1, n):
        if j in dic[i]:
            continue
        for k in range(j+1, n+1):
            if k in dic[i] or k in dic[j]:
                continue
            answer += 1
print(answer)