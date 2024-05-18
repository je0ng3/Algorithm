def solution(nums):
    total = len(nums)
    nums = set(nums)
    if total/2 <= len(nums):
        answer = total/2
    else:
        answer = len(nums)
    return answer