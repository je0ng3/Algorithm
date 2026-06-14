def solution(elements):
    n = len(elements)
    arr = elements*2
    sums = set()
    
    for leng in range(1, n+1):
        for i in range(n):
            sums.add(sum(arr[i:i+leng]))
    return len(sums)