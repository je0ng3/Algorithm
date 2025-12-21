a, b, c, n = map(int, input().split())

if n%c%b%a == 0:
    print(1)
else:
    print(0)