def solution(n, w, num):
    answer = 0
    height = n//w
    extra = n%w
    num_f = num//w
    if num%w>0:
        num_f += 1
    answer = height-num_f+1
    
    if extra == 0:
        return answer
    
    idx_num = w-(num_f*w-num) if num_f%2==1 else num_f*w-num + 1
    idx_extra = w-extra+1 if (height+1)%2==0 else extra
    
    if (height+1)%2==0:
        if idx_extra <= idx_num:
            answer += 1
    else:
        if idx_extra >= idx_num:
            answer += 1
            
    return answer