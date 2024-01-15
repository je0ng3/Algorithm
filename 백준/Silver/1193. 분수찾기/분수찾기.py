import sys

n = int(sys.stdin.readline())
sigma = 0
count = 0
molecule = [0]
denominator = [0]
for i in range(1, n+1):
  sigma += i
  if n <= sigma:
    count = i
    sigma -= i
    break
if count%2 == 0:
  molecule += range(1, count+1)
  denominator += range(1,count+1)[::-1]
else:
  molecule += range(1,count+1)[::-1]
  denominator += range(1,count+1)
print(molecule[n-sigma],'/',denominator[n-sigma], sep='')
