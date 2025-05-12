def solution(arr):
    dq = []
    last = arr[0]
    dq.append(last)
    for i in arr[1:]:
        if last!=i:
            dq.append(i)
            last = i
    return dq