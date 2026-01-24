def solution(n):
    answer = n+1
    count_0 = format(n, 'b').count('1')
    while True:
        if format(answer, 'b').count('1')==count_0:
            break
        answer += 1
    return answer