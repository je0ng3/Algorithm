m = int(input())
n = int(input())

mini = -1
psn = []
for i in range(m, n + 1):
    temp = i ** (1 / 2)
    if int(temp) == temp:
        if mini == -1:
            mini = i
        psn.append(i)
if psn:
    print(sum(psn))
print(mini)
