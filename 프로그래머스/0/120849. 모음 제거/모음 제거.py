def solution(my_string):
    answer = ''
    d = ['a', 'e', 'i', 'o', 'u']
    ms = list(my_string)
    for i in ms:
        if i in d:
            continue
        answer+=i
    return answer