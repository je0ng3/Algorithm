import sys

n, m = map(int, sys.stdin.readline().split())
poketmon = []
for _ in range(n):
  poketmon.append(sys.stdin.readline().rstrip())
for _ in range(m):
  find = sys.stdin.readline().rstrip()
  if find.isdigit():
    find = int(find)
    print(poketmon[find-1])
  else:
    print(poketmon.index(find)+1)