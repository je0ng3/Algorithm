N = int(input())
t = []
w = []

for _ in range(N):
    time, pos = input().split()
    t.append(int(time))
    w.append(pos)

# Please write your code here.
# A B C D : 본인 앞의 인덱스에 차가 없을 때 출발
from collections import deque

idx, now = 0, 0
cars = [0,0,0,0] # A B C D
cars_idx = {'A':0, 'B':1, 'C':2, 'D':3}
q = [deque() for _ in range(4)] # 대기 차량
answer = [-1 for _ in range(N)]

while idx < N:
    if sum(cars)==0:
        now = t[idx]

    while idx<N and now==t[idx]:
        pos_idx = cars_idx[w[idx]]
        cars[pos_idx]+=1
        q[pos_idx].append(idx)
        idx +=1
    if 0 not in cars:
        break

    go = [1 if cars[i-1]==0 else 0 for i in range(4)]
    for i, g in enumerate(go):
        if g and cars[i]:
            cars[i]-=1
            out = q[i].popleft()
            answer[out] = now
    now += 1

while sum(cars)>0 and sum(go)>0:
    go = [1 if cars[i-1]==0 else 0 for i in range(4)]
    for i, g in enumerate(go):
        if g>0 and cars[i]>0:
            cars[i]-=1
            out = q[i].popleft()
            answer[out] = now
    now += 1

for a in answer:
    print(a)