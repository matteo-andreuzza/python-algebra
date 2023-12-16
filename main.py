a = ''
b = ''

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
op = ['-']
num = ['1','2','3','4','5','6','7','8','9']
lett = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import re

def fil(lista):
    # Utilizza la list comprehension e regex per filtrare numeri, lettere e espressioni alfanumeriche
    lista_filtrata = [elemento for elemento in lista if re.search(r'[a-zA-Z0-9]', str(elemento))]
    return lista_filtrata

def algsum(d):
    fi = []
    t1 = ''
    t2 = ''
        
    print(d)
    c =fil(d)
    print('filt '+str(c))
    l = len(c)        
    for i in range(l-1):
        try:
            t1 = c[i]
            t2 = c[i+1]
            c.pop(i+1)
            l = l-1
            c[i] = sum(t1,t2)
        except IndexError:
            t1 = c[i-1]
            t2 = c[i-2]
            c.pop(i-2)
            l = l-1
            c[i-2] = sum(t1,t2)
    return c
        
        
def sum(x,y):
    q = ''
    q2 = ''
    w = ''
    w2 = ''
    esp1 = 0
    esp2 = 0
    c = 0
    if x[0] != "-" and x[0] not in num:
        t = list(x)
        t.insert(0, '1')
        x = ''
        for z in t:
            x += str(z)
        if y[0] != "+" or y[0] != "":
            t = list(y)
            t.insert(0, '1')
        y = ''
        for z in t:
            y += str(z)
    for i in range(len(x)):
        if x[i] == '^':
            esp1 = i
    for i in x:
        if c < esp1:
            try:
                if i == '-':
                    continue
                if type(int(i)) == int and x[c] == '-':
                    q += '-'+i
                else:
                    q += i
            except ValueError:
                q2 += i
        else:
            q2 += i
        c = c+1
    c = 0
    i = 0
    for i in range(len(y)):
        if y[i] == '^':
            esp2 = i
    for i in y:
        if c < esp2:
            try:
                if i == '-':
                    continue
                if type(int(i)) == int and y[c] == '-':
                    w += '-'+i
                else:
                    w +=i
                
            except ValueError:
                w2 += i
        else:
            w2 += i
            
        c = c+1
    if q2 == w2 and int(q)+int(w) != 0:
        return str((int(q)+int(w))) + q2
    elif int(q) + int(w) == 0:
        return ''
    else:
        return 'impossibile sommare termini con lettere diverse'

print(molt('4ab', '2ab'))