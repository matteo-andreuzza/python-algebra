#! nuovo file della moltiplicazione, commento tutto

from aggr import aggr
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
num = ['1','2','3','4','5','6','7','8','9','-']


#! moltiplicazione di parti letterali di due monomi, restituisce stringa

def molt(a,b):
    if len(a)>len(b):
        return molt(b,a)
    else:
        t = [] #? t array da returnare
        s = 0
        bt = []
        for i in b:
            bt.append(i)
        for i in range(len(a)):
            k = i - s
            l = a[i] #? l scrorre a
            l2 = b[k] #? l2 scorre b
            if l in lett:#? controlla in lett altrimenti prende anche ^
                if l in b and l in lett: 
                    if IsEsp(i,a) and IsEsp(k,b): #* se entrambi esp
                        t.append(l+'^'+str(esp(i,a) + esp(k,b)))
                        b.pop(b.index(l2))
                        b.pop(b.index(b[k]))
                        b.pop(b.index(b[k]))
                        s = s + 1
                    elif IsEsp(i,a) and IsEsp(k,b) == False:
                        t.append(l + '^' + str(esp(i,a) + 1))
                        b.pop(b.index(l2))
                        s = s + 1
                    elif IsEsp(i,a) == False and IsEsp(k,b):
                        t.append(l+'^'+str(esp(k,b) + 1))
                        b.pop(b.index(l2))
                        b.pop(b.index(b[k]))
                        b.pop(b.index(b[k]))
                        s = s + 1
                    else:
                        t.append(l+'^'+'2')
                        b.pop(b.index(l2))
                        s = s+1
                else:
                    if IsEsp(i,a):
                        t.append(a[i])
                        t.append(a[i+1])
                        t.append(a[i+2])
                    else:
                        t.append(l)
            else:
                s = s+1 # aumenta s così se l non è lettera allora b non rimane indietro
                continue
        for i in b:
            t.append(i)
        return aggr(t,'s') #aggrego l'array, restituendo una stringa.


def algmolt(a,b):
#    print(f""" 
#        MOLTIPLICAZIONE ****
#        DI   {aggr(a,'s')} * {aggr(b,'s')}
#    """)
    flag = False
    z = []
    a1 = ''
    b1 = ''
    d = 0
    while a[d-d] in num:
        a1 = a1 + str(a[d-d])
        a.pop(d-d)
        d = d+1
    if a1 != '':
        a1 = int(a1)
    else:
        a1 = 0
    if a1 == 0:
        a1 = 1
    d = 0
    while b[d-d] in num:
        b1 = b1 + str(b[d-d])
        b.pop(d-d)
        d = d+1
    if b1 != '':
        b1 = int(b1)
    else:
        b1 = 0
    if b1 == 0:
        b1 = 1
    if a1 != 0 and b1 != 0:
        if (a1*b1) < 0:
            z.append(str(a1*b1))
            flag = True
        elif (a1*b1) == 1:
            pass
        else:
            z.append('+' + str(a1*b1))
            flag = True
    z.append(molt(listpol(aggr(a,'s')),listpol(aggr(b,'s'))))
    if flag == False:
        return '+' + aggr(z,'s')
    else:
        return aggr(z,'s')
        
    
print(algmolt(listpol("6ab"), listpol("2ab")))
print(algmolt(listpol('a^3b^2'), listpol('a^2c^3')))
print(algmolt(listpol('ab'), listpol('ab')))
print(algmolt(listpol('a^3b^2'), listpol('a^2c^3')))
print(algmolt(listpol('x^2y^3'), listpol('x^3m^2')))
print(algmolt(listpol('p^4q^5'), listpol('p^3r^4')))
print(algmolt(listpol('p^4q^5z^3d^22'), listpol('p^4q^5')))
print(algmolt(listpol('12x'), listpol('3x')))
print(algmolt(listpol('a^2b^2'), listpol('2ac')))
