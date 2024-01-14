import sys

n, m = map(int, sys.stdin.readline().split())
basket = list(range(1, n+1))
for _ in range(m):
  i, j = map(int, sys.stdin.readline().split())
  i, j = i-1, j-1
  basket[i:j+1] = basket[i:j+1][::-1]
print(*basket)