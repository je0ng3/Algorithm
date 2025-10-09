import itertools

def solution(friends, gifts):
    record = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    for gift in gifts:
        give, given = gift.split(' ')
        record[friends.index(given)][friends.index(give)]+=1
    # 친구들의 선물지수
    gift_level = check_level(friends, record)
    # 다음달에 받을 선물 개수 
    next_gift = {friend:0 for friend in friends}
    for a, b in itertools.combinations(friends, 2):
        a_give, b_give = give_count(a, b, friends, record)
        given = who_given(a, b, a_give, b_give, gift_level)
        if given != -1:
            next_gift[given] +=1
    return max(next_gift.values())
    
# 모든 친구들의 선물지수
def check_level(friends, record):
    cl = {friend:0 for friend in friends}
    for i, friend in enumerate(friends):
        cl[friend] += sum([x[i] for x in record]) # + 준 개수
        cl[friend] -= sum(record[i]) # - 받은 개수
    return cl

# a->b, b->a 선물 준 개수
def give_count(a, b, friends, record):
    a_idx = friends.index(a)
    b_idx = friends.index(b)
    return (record[b_idx][a_idx], record[a_idx][b_idx])

# a와 b 중 선물받을 사람
def who_given(a, b, a_give, b_give, gift_level):
    if a_give<b_give:
        return b
    if a_give>b_give:
        return a
    if gift_level[a]<gift_level[b]:
        return b
    if gift_level[b]<gift_level[a]:
        return a
    return -1
    