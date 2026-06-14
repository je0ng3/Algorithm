def solution(arr):
    answer = 1
    all_pf = {}
    for cur in arr:
        cur_pf = pf(cur)
        for key, val in cur_pf.items():
            if key in all_pf:
                all_pf[key] = max(all_pf[key], val)
            else:
                all_pf[key]= val
    for key, val in all_pf.items():
        answer*= key**val
    return answer

def pf(num):
    temp = {}
    d = 2
    while d*d<=num:
        while num%d==0:
            if d in temp:
                temp[d] +=1
            else:
                temp[d] = 1
            num//=d
        d+=1
    if num>1:
        temp[num] = 1
    return temp