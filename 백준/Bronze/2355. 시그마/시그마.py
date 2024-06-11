import sys
a, b = map(int,sys.stdin.readline().rstrip().split())
if a>b:
    a, b = b,a
sum_a = (a-1)*a//2
sum_b = (b+1)*b//2
print(sum_b-sum_a)