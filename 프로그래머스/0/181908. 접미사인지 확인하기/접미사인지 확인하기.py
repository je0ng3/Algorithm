def solution(my_string, is_suffix):
    answer = 0
    length = len(my_string)-len(is_suffix)
    if length>=0:
        if my_string[length:] == is_suffix:
            answer =1
    return answer