def solution(nums):
    types = len(set(nums))
    allowed = len(nums)/2
    if types>allowed:
        return allowed
    return types