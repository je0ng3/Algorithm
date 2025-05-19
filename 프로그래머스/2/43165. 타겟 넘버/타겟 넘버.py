def solution(numbers, target):
    a = [numbers[0], -numbers[0]]
    for i in numbers[1:]:
        plus = [j+i for j in a]
        minus = [j-i for j in a]
        a = plus + minus
    return a.count(target)