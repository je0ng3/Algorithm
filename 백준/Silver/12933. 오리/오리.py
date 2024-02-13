quack = list(input())
index = ['q','u','a','c','k']
count = []
f = 0
for i in range(len(quack)):
  sound = quack[i]
  s_i = index.index(sound)
  if s_i == 0:
    if 4 in count:
      count[count.index(4)] = 0
    else:
      count.append(0)
  else:
    if (s_i-1) in count:
      count[count.index(s_i-1)] += 1
    else:
      f = -1
      break

for i in count:
  if i != 4:
    f = -1
    break
if f==-1:
  print(-1)
else:
  print(len(count))