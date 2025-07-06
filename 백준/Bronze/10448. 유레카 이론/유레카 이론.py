t = int(input())
tri = [i * (i + 1) // 2 for i in range(1, 45)]
for _ in range(t):
    k = int(input())
    check = 0
    for i in range(1, k // 3 + 1):
        if i not in tri:
            continue
        for j in range(1, k - i+ 1):
            if j not in tri:
                continue
            if k - (i + j) in tri:
                check = 1
                break
        if check == 1:
            break
    print(check)
