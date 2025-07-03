def makeSet(s):
    ms = set()
    ml = []
    s = s.lower()
    for i in range(len(s) - 1):
        a = s[i : i + 2]
        if a.isalpha():
            ms.add(a)
            ml.append(a)
    return ms, ml

def solution(str1, str2):
    setS1, ls1 = makeSet(str1)
    setS2, ls2 = makeSet(str2)

    if len(setS1) == 0 and len(setS2) == 0:
        return 65536

    intersec = setS1.intersection(setS2)
    uni = setS1.union(setS2)

    countI = 0
    for i in intersec:
        countI += min(ls1.count(i), ls2.count(i))
    countU = 0
    for i in uni:
        countU += max(ls1.count(i), ls2.count(i))

    return int(countI / countU * 65536)