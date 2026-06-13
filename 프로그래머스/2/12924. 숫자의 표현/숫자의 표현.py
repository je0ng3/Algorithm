def solution(n):
    answer = 0
    
    left, right = 1, 1
    cur_sum = 1
    while left<=n:
        if cur_sum==n:
            answer += 1
            cur_sum-=left
            left+=1
        elif cur_sum<n:
            right += 1
            cur_sum += right
        else: # cur_sum >n
            cur_sum -= left
            left += 1
            
    return answer