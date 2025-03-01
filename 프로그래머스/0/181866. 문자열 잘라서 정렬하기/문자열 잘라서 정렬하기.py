def solution(myString):
    s_list = myString.split('x')
    answer = [i for i in s_list if i!='']
    return sorted(answer)