def solution(my_string):
    a = list(my_string.split())
    answer = 0
    plus = 0
    minus = 0
    for i in a:
        if i=="+":
            plus = 1
        elif i=="-":
            minus = 1
        elif plus:
            answer += int(i)
            plus = 0
        elif minus:
            answer -= int(i)
            minus = 0
        else:
            answer += int(i)
    return answer