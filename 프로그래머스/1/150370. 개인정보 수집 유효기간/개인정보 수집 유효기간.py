def solution(today, terms, privacies):
    answer = []
    today = str_to_day(today)
    td = term_to_day(terms)
    exp_day = exp(td, privacies)
    for idx, ed in enumerate(exp_day, 1):
        if ed<=today:
            answer.append(idx)
    return answer

def exp(td, privacies):
    ed = []
    for privacy in privacies:
        agree, term = privacy.split(' ')
        experience = str_to_day(agree) + td[term]
        ed.append(experience)
    return ed
        
def term_to_day(terms):
    td = {}
    for term in terms:
        type, month = term.split(' ')
        td[type] = int(month)*28
    return td

def str_to_day(str):
    y, m, d = map(int, str.split('.'))
    return (y*12+m)*28+d