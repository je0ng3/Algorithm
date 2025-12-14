def solution(lottos, win_nums):
    match = len(set(lottos) & set(win_nums))
    unknown = lottos.count(0)
    highst = min(7-(match+unknown), 6)
    lowst = min(7-match, 6)
    return [highst, lowst]