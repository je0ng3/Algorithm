def solution(topping):
    answer = 0
    left = set()
    right = {}
    for t in topping:
        if t in right:
            right[t]+=1
        else:
            right[t]=1
    
    for t in topping:
        left.add(t)
        right[t]-=1
        if right[t]==0:
            del right[t]
        
        if len(left)==len(right):
            answer += 1
        
    return answer

# 두 조각으로 잘라
# 각 조각에 동일한 가짓수의 토핑이 올라가면 공평하게 롤케이크가 나누어진 것
# 롤케이크를 공평하게 자르는 방법의 수