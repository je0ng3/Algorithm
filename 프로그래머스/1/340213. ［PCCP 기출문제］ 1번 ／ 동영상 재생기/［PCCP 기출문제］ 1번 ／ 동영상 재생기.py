def solution(video_len, pos, op_start, op_end, commands):
    vl, p, os, oe = t2s(video_len), t2s(pos), t2s(op_start), t2s(op_end)
    if os<=p and p<oe:
        p=oe
    for command in commands:
        if command == "prev":
            p = max(0, p-10)
        elif command == "next":
            p = min(vl, p+10)
        if os<=p and p<oe:
            p=oe
    return s2t(p)

def t2s(time):
    (m, s) = map(int,time.split(":"))
    return s+m*60

def s2t(ss):
    m = str(ss//60)
    s = str(ss%60)
    if len(m)==1:
        m = "0"+m
    if len(s)==1:
        s = "0"+s
    return m+":"+s