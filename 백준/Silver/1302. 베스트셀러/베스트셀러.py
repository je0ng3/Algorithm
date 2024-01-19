import sys

n = int(sys.stdin.readline())
title = {}
for _ in range(n):
  book = sys.stdin.readline().strip()
  if book not in title:
    title[book] = 1
  else:
    title[book] += 1
sorted_title = sorted(title.items(), key=lambda x: (-x[1], x[0]))
print(sorted_title[0][0])