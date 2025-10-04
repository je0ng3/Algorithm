def solution(new_id):
    answer = '.'
    for id in list(new_id):
        if id.isalpha():
            answer+=id.lower()
        elif (id=='.' and answer[-1]!='.') or (id in ['-', '_']):
            answer+=id
        elif id.isdigit():
            answer+=id
    answer = answer[1: min(16, len(answer))]
    answer = answer.rstrip('.')
    if answer=='':
        answer+='a'
    while len(answer)<3:
        answer+=answer[-1]
    return answer