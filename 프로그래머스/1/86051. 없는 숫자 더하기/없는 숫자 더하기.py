def solution(numbers):
    answer = 0
    numbers.sort()
    for i in range(10):
        if i>=len(numbers):
            answer += i
        elif i != numbers[i]:
            answer += i
            numbers = [0]+numbers
    return answer