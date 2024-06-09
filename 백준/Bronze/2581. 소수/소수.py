m = int(input())
n = int (input())
arr = [i for i in range(n+1)]
arr[0] = 0
arr[1] = 0
for i in range(2, int(n**(1/2))+1):
    if arr[i]==0:
        continue
    for j in range(i*i, n+1, i):
        arr[j] = 0
a = [i for i in arr[m:] if arr[i]]
if len(a)>0:
    print(sum(a))
    print(a[0])
else:
    print(-1)