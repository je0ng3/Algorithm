def solution(my_string):
    answer = 0
    n = ''
    for i in range(len(my_string)):
        if(my_string[i].isdigit()):
            n+=my_string[i]
        elif len(n)>0:
            answer+=int(n)
            n = ''
    if len(n)>0:
        answer+=int(n)
    return answer