def solution(my_string, letter):
    answer = ''
    ms = list(my_string)
    for i in ms:
        if i==letter:
            continue
        answer+=i
    return answer