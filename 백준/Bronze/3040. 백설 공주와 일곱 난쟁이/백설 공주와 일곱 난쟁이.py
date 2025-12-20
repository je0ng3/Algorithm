l = []
for _ in range(9):
    l.append(int(input()))
all = sum(l)
check = 0
for i in range(8):
    x = l[i]
    for j in range(i+1, 9):
        y = l[j]
        if all-(x+y)==100:
            l.remove(x)
            l.remove(y)
            check = 1
            break
    if check:
        break
for i in l:
    print(i)