def solution(my_string, indices):
    indices.sort()
    i = 0
    my_string = list(my_string)
    for j in indices:
        del(my_string[j-i])
        i+=1
    return ''.join(my_string)