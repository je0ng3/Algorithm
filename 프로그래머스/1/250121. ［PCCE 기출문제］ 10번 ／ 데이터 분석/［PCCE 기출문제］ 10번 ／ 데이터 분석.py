def solution(data, ext, val_ext, sort_by):
    answer = []
    label = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }
    for info in data:
        if info[label[ext]]<val_ext:
            answer.append(info)
    return sorted(answer, key=lambda x : x[label[sort_by]])