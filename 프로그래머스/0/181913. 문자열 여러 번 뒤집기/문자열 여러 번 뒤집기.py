def solution(my_string, queries):
    query = queries[0]
    for query in queries:
        my_string = my_string[:query[0]]+(my_string[query[0]:min(len(my_string),query[1]+1)])[::-1]+my_string[query[1]+1:]
    return my_string



