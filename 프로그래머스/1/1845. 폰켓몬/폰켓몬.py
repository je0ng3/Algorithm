def solution(nums):
    answer = 0
    set_num = set(nums)
    answer = min(len(set_num), len(nums)//2)
    return answer