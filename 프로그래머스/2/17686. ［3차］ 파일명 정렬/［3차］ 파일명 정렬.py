def solution(files):
    files = [split_name(file) for file in files]
    files = sorted(files, key=lambda x: (x[0].upper(), int(x[1])))
    return [''.join(file) for file in files]

# 파일명 -> [head, number, tail]
def split_name(file):
    head = number = tail = ""
    check = 0
    for x in list(file):
        if check:
            tail+=x
        elif x.isdigit() and len(number)<5:
            number+=x
        elif not x.isdigit() and len(number)>0:
            tail+=x
            check = 1
        else:
            head+=x
    return [head, number, tail]
            