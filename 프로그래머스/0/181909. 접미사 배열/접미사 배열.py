def solution(my_string):
    answer = [my_string[i:] for i in range(0,len(my_string))]
    return sorted(answer)