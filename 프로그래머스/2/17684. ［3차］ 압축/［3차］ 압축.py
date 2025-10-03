def solution(msg):
    answer = []
    words = [chr(i+65) for i in range(26)]
    while len(msg)>0:
        idx, msg, words = find_msg(msg, words)
    # return (idx, msg, words)
        answer.append(idx)
    return answer

def find_msg(msg, words):
    temp = ''
    check = 0
    for i in list(msg):
        temp += i
        if temp not in words:
            words.append(temp)
            check = 1
            break
    if check:
        return (words.index(temp[:-1])+1, msg[len(temp)-1:], words)
    else:
        return (words.index(temp)+1, '', words)