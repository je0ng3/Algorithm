n= int(input())
B=[1,1]
if n==1 or n==2:
    print(1)
else:
    for i in range(2,n):
        B.append(B[i-1]+B[i-2])
    print(B[n-1])