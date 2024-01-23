from listmut import el
from listpol import listpol
def IsEsp(index, arr):
    try:
        if arr[index+1] == '^':
            return True
        else:
            return False
    except IndexError:
        return False

def esp(index, arr):
    return int(arr[index + 2])
lett = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def molt(a,b):
    t = []
    s = 0
    k = 0
    j = 0
    us = False
    for i in range(len(a)):
        if(len(a) == len(b) == 3) and us == True:
            t.append((molt(a,b)[0]))
            return t
        us = True
        k = i-s
        try:
            l = a[i]
        except IndexError:
            try:
                l = a[-1]
                i = -1
            except IndexError:
                for i in range(len(b)):
                    if IsEsp(i,b):
                        t.append(b[i])
                        t.append(b[i+1])
                        t.append(b[i+2])
                    else:
                        if b[i] in lett:
                            t.append(b[i])
                        else:
                            continue
        try:
            l2 = b[k]
        except:
            try:
                l2 = b[-1]
                k = -1
            except IndexError:
                for i in range(len(a)):
                    if IsEsp(i,a):
                        t.append(a[i])
                        t.append(a[i+1])
                        t.append(a[i+2])
                    else:
                        if a[i] in lett:
                            t.append(a[i])
                        else:
                            continue
                break

        if l in lett and l2 in lett:
            try:
                if l in b:
                    if IsEsp(i, a) and IsEsp(k,b):
                        t.append(l+'^'+str(esp(i,a)+esp(k,b)))
                        b.pop(b.index(l2))
                        b.pop(k)
                        b.pop(k)
                        a.pop(a.index(l))
                        a.pop(i)
                        a.pop(i)
                    elif IsEsp(i,a) and IsEsp(k,b) == False:
                        t.append(l+'^'+str(esp(i,a)+1))
                        b.pop(b.index(l2))
                        a.pop(a.index(l))
                        
                        
                    elif IsEsp(i,a) == False and IsEsp(k,b):
                        t.append(l+'^'+str(esp(k,b)+1))
                        b.pop(b.index(l2))
                        b.pop(k)
                        b.pop(k)
                        a.pop(a.index(l))
                        a.pop(i)
                        a.pop(i)
                    else:
                        t.append(l+'^'+'2')
                        b.pop(b.index(l2))
                        a.pop(a.index(l))
                        

                        
                else:
                    if IsEsp(i,a):
                        t.append(a[i])
                        t.append(a[i+1])
                        t.append(a[i+2])
                    else:
                        if b[i] in lett:
                            t.append(a[i])
                        else:
                            continue
            except IndexError:
                pass
            print(t)

        else:
            continue
    for i in range(len(b)):
        if IsEsp(i,b):
            t.append(b[i])
            t.append(b[i+1])
            t.append(b[i+2])
        else:
            if b[i] in lett:
                t.append(b[i])
            else:
                continue
    
    return t

print(molt(listpol('a^3b^2'), listpol('a^2c^3')))
print(molt(listpol('b^2'), listpol('c^3')))

