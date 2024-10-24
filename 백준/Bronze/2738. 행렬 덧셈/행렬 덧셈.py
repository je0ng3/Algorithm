n, m = map(int,input().split())
a = []
for _ in range(n):
  c = list(map(int, input().split()))
  a.append(c)
result = []
for i in range(n):
  d = list(map(int, input().split()))
  result.append([x+y for x, y in zip(a[i], d)])
for row in result:
  print(" ".join(map(str, row)))