def solution(users, emoticons):
    plus = result = 0
    discount = [10, 20, 30, 40]
    emos = dfs(0, [], [], emoticons, discount)
    for emo in emos:
        p, r = purchase(users, emo)
        if plus<p:
            plus, result = p, r
        elif plus==p and result<r:
            result = r
    return [plus, result]

# 모든 가능한 이모티콘 가격 조합
def dfs (idx, current, emos, emoticons, discount):
    if idx == len(emoticons):
        emos.append(current[:])
        return 
    for d in discount:
        discounted = emoticons[idx]*(100-d)/100
        current.append((d, discounted))
        dfs(idx + 1, current, emos, emoticons, discount)
        current.pop()
    return emos

# 해당 이모티콘 상태일 때, [이모티콘 플러스 가입자 수, 판매액]
def purchase(users, emo):
    p = r = 0
    for user in users:
        temp = 0
        for rate, price in emo:
            if user[0]>rate:
                continue
            temp += price
        if temp < user[1]:
            r += temp
        else:
            p += 1
    return [p, r]