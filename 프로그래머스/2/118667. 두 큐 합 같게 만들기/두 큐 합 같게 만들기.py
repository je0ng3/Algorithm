from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    if (sum(queue1)+sum(queue2))%2!=0:
        return -1
    
    target = (sum1+sum2)//2 
    if max(queue1)>target or max(queue2)>target:
        return -1
    
    max_ops = len(queue1)*3
    for i in range(max_ops):
        if sum1==sum2:
            return i
        if sum1>sum2:
            x = q1.popleft()
            q2.append(x)
            sum1 -= x
            sum2 += x
        else:
            x = q2.popleft()
            q1.append(x)
            sum1 += x
            sum2 -= x
    return -1