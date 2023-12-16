
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