def solution(diffs, times, limit):
    answer = 0
    left, right = 1, max(diffs)
    while left <= right:
        mid = (left+right)//2
        if cal(diffs, times, limit, mid): # 더 작은쪽도 탐색
            answer = mid
            right = mid - 1
        else: # 더 큰쪽 탐색
            left = mid + 1
    return answer

def cal(diffs, times, limit, level):
    temp = 0
    time_prev = 0
    for diff, time in zip(diffs, times):
        if temp>limit:
            break
        if diff<=level:
            temp += time
        else:
            temp += (time_prev+time)*(diff-level)+time
        time_prev = time
    if temp <= limit:
        return True
    return False