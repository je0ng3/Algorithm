from collections import deque

def solution(order):
    answer = 0
    stack = deque()
    new_box = 1
    while new_box<=len(order):
        if new_box==order[answer]: # 메인 컨테이너 -> 트럭
            answer += 1
            new_box += 1
        elif stack and stack[-1]==order[answer]: # 보조 컨테이너 -> 트럭
            stack.pop()
            answer += 1
        else:
            stack.append(new_box)
            new_box += 1
    
    # 메인 끝, 남은 보조 컨테이너 확인
    while stack and answer < len(order):
        if stack[-1] == order[answer]:
            stack.pop()
            answer += 1
        else:
            break
        
    return answer