t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))
    order = [i for i in range(n)]
    num = 1
    while docs:
        max_val = max(docs)
        a = docs.pop(0)
        b = order.pop(0)
        if a != max_val:
            docs.append(a)
            order.append(b)
        elif b == m:
            print(num)
            break
        else:
            num += 1
