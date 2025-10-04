def solution(record):
    nickname = {}
    order = []
    for r in record:
        part = r.split(' ')
        if part[0]!="Leave":
            nickname[part[1]]=part[2]
        if part[0]!="Change":
            order.append([part[0], part[1]])
    answer = []
    for in_out, user_id in order:
        if in_out == 'Enter':
            answer.append(nickname[user_id]+"님이 들어왔습니다.")
        else:
            answer.append(nickname[user_id]+"님이 나갔습니다.")
    return answer