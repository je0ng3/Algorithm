import sys

n, m = map(int, sys.stdin.readline().split())
basket = list(range(1, n+1))
for _ in range(m):
  i, j = map(int, sys.stdin.readline().split())
  basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
print(*basket)