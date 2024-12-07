def solution(arr, queries):
    answer = []
    for query in queries:
        a = arr[query[0]:query[1]+1]
        a = [i for i in a if i>query[2]]
        if len(a)>0:
            answer.append(min(a))
        else:
            answer.append(-1)
    return answer