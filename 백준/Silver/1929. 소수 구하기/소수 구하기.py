import sys
import math

m, n = map(int,sys.stdin.readline().split())
a = 1 if m%2==0 else 0
pn = []
if m<= 2 and n >= 2:
    pn.append(2)
for i in range(m+a, n+1, 2):
  count = 0
  for j in range(2, int(math.sqrt(i))+1):
    if i % j == 0:
      count += 1
      break
  if count == 0 and i != 1:
    pn.append(i)
pn.sort(reverse=False)
for i in pn:
    print(i)