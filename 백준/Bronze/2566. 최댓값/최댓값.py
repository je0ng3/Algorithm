maxNum = -1
row, col = 0, 0
for i in range(1,10):
  a = list(map(int, input().split()))
  if maxNum < max(a):
    row = i
    col = a.index(max(a)) + 1
    maxNum = max(a)
print(maxNum)
print(row, col)
