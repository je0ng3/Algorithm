import itertools


def solution(user_id, banned_id):
    answer = []
    sets = []
    for ban in banned_id:
        sets.append({user for user in user_id if match(user, ban)})
    for combo in itertools.product(*sets):
        if len(combo)!=len(set(combo)) or len(combo)!=len(sets):
            continue
        temp = sorted(list(combo))
        if temp not in answer:
            answer.append(temp)
    return len(answer)

def match(user, ban):
    if len(user)!=len(ban):
        return False
    for u, b in zip(user, ban):
        if b == '*':
            continue
        if u != b:
            return False
    return True