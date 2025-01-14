def solution(my_string):
    answer = []
    for i in list(my_string):
        if i.isdigit():
            answer.append(i)
    return list(map(int,sorted(answer)))