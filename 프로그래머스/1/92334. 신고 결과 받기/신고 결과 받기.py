def solution(id_list, report, k):
    member = {mem:[] for mem in id_list}
    for r in set(report):
        a, b = r.split(' ')
        member[b].append(a)
    counts = {mem:0 for mem in id_list}
    for mem, by in member.items():
        if len(by)<k:
            continue
        for b in by:
            counts[b]+=1
    return list(counts.values())