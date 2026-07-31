from collections import Counter

def solution(participant, completion):
    temp = Counter(participant) - Counter(completion)
    return list(temp.keys())[0]