from itertools import permutations

def solution(numbers):
    answer = 0
    cases = [''.join(i)  for j in range(1, len(numbers)+1) for i in permutations(list(numbers), j)]
    for case in list(set(map(int, cases))):
        if is_prime(case):
            answer+=1
    return answer

def is_prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True