def solution(my_string):
    answer = 0
    ms = list(my_string)
    for i in ms:
        if i.isdigit():
            answer+=int(i)
    return answer