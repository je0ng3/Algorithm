def solution(my_string, n):
    answer = ''
    for i in list(my_string):
        answer+=i*n
    return answer