n = int(input())
a = list(input())
for i in range(n-1):
    b = list(input())
    for idx, j in enumerate(b):
        if a[idx]!=j:
            a[idx]='?'
print(''.join(a))