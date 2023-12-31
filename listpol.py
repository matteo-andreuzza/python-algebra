def listpol(a):
    a+='m' #! IMPORTANTE, lasciare perchè altrimenti fa IndexError alla fine
    num = ['1','2','3','4','5','6','7','8','9']
    lett = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    b = []
    k = ''
    t = 2
    st = ''
    gt = 0
    it = 0
    i = 0
    while i < len(a):
        k = ''
        t = 2
        st = ''
        gt = 0
        it = 0
        try:
            gt = a[i + 1]
        except IndexError:
            gt = 0
        if gt == '^':
            b.append(a[i])
            b.append(a[i+1])
            it = i
            try:
                i = i+1
                k = a[it+t]
                while a[it+t] not in lett:
                    k = a[it+t]
                    st += k
                    t = t + 1
                    i = i+1
                b.append(st)
                st = ''
            except IndexError:
                try:
                    i = i+1
                    k = a[it+t-1]
                    while a[it+t-1] not in lett:
                        k = a[it+t-1]
                        st += k
                        t = t + 1
                        i = i+1
                    b.append(st)
                    st = ''
                except IndexError:
                    pass
        else:
            try:
                b.append(a[i])
            except IndexError:
                pass
        i = i + 1
    b.pop(-1) #! IMPORTANTE, lasciare perchè rimuove lettera temporanea per non fare IndexError
    return b
