sum = 0
mushroom = [int(input()) for _ in range(10)]
for mush in mushroom:
    if abs(100 - (sum + mush)) <= abs(100 - sum):
        sum += mush
    else:
        break
print(sum)
