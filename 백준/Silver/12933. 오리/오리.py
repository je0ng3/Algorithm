quack = list(input())
count = []
f = 0
for i in range(len(quack)):
  if quack[i] == 'q':
    if 4 in count:
      count[count.index(4)] = 0
    else:
      count.append(0)
  elif quack[i] == 'u':
    if 0 in count:
      count[count.index(0)]+=1
    else:
      f = -1
      break
  elif quack[i] == 'a':
    if 1 in count:
      count[count.index(1)]+=1
    else:
      f = -1
      break
  elif quack[i] == 'c':
    if 2 in count:
      count[count.index(2)]+=1
    else:
      f = -1
      break
  elif quack[i] == 'k':
    if 3 in count:
      count[count.index(3)]+=1
    else:
      f = -1
      break
  else:
    f = -1
    break

for i in count:
  if i != 4:
    f = -1
    break
    
if f!=-1:
  print(len(count))
else:
  print(-1)
