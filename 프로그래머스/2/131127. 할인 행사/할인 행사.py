
def solution(want, number, discount):
    answer = 0
    target = dict(zip(want, number))
    
    # 처음 10일
    window = {}    
    for item in discount[:10]:
        window[item] = window.get(item, 0) +1    
    if window == target:
        answer += 1
        
    for i in range(10, len(discount)):
        left = discount[i-10]
        right = discount[i]
        
        window[left] -= 1
        if window[left] == 0:
            del window[left]
        window[right] = window.get(right, 0) + 1
        
        if window == target:
            answer += 1
            
    return answer