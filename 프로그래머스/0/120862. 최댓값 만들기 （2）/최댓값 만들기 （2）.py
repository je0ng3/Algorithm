def solution(numbers):
    answer = numbers[0]*numbers[1]
    for idx, i in enumerate(numbers[:-1]):
        for j in numbers[idx+1:]:
            answer = max(answer, i*j)
    return answer