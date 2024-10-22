n = int(input())
list = []
for _ in range(n):
  a = int(input())
  list.append(a)
list.sort()
for i in list:
  print(i)