a, b, c, n = map(int, input().split())

possible = 0
for i in range(n//a+1):
    for j in range(n//b+1):
        rest = n - (a*i + b*j)
        if rest >=0 and rest%c == 0:
            possible = 1
            break
    if possible:
        break
print(possible)