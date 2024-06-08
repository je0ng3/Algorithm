while True:
    try:
        m= list(map(ord,list(input())))
        m.sort()
        c, b, n, s = 0,0, 0, 0
        for i in m:
            if i==32:
                s+=1
            elif i<58:
                n+=1
            elif i<91:
                b+=1
            else:
                c+=1
        print(c, b, n, s)
    except EOFError:
        break