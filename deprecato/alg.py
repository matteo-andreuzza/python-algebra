
def algsum(d):
    print(d)
    c =fil(d)
    print('filt '+str(c))
    l = len(c)        

    for i in range(l-1):
        print(c)
        
        print("c"+c[i])
        t1 = c[i]
        try:
            t2 = c[i+1]
            c.pop(i+1)
            l = l-1
        except IndexError:
            try:
                t2 = c[i-1]
                c.pop(i-1)
                l = l-1
                
            except IndexError:
                pass
        try:
            c[i] = sum(t1,t2)
            print(c)
        except IndexError:
            c[i-1] = sum(t1,t2)
            print(c)
            
        t1 = ''
        t2 = ''
    return c




def molt(x,y):
    ret = ''
    q = ''
    q2 = ''
    w = ''
    w2 = ''
    for i in x:
        try:
            if type(int(i)) == int:
                q += i
        except ValueError:
            q2 += i
    for i in y:
        try:
            if type(int(i)) == int:
                w += i
        except ValueError:
            w2 += i
    if q2 != w2:      
        r = str((int(q)*int(w))) + q2 + w2
        print('r' + r)
        es = 0
        ret = list(r)
        for i in range(len(ret)):
            try:
                if ret[i] == ret[i+1]:
                    for k in range(len(ret)-i):
                        try:
                            if ret[k] == ret[k+1]:
                                es = es + 1
                                ret.pop(k+1)
                        except IndexError:
                            pass
                    ret[i] = ret[i] + '^' + str(es+1)
            except IndexError:
                pass
        r = ''
        for i in ret:
            r += i
        return r
    else:
        return str(int(w)*int(q))+str(q2) + '^2'