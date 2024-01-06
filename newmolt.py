#! nuovo file della moltiplicazione, commento tutto

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
    t = [] #? t array da returnare
    s = 0
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
    return t
print('a^3b^2 * a^2c^3 = ' + str(molt(listpol('a^3b^2'), listpol('a^2c^3'))))
print('b^2 * c^3 = ' + str(molt(listpol('b^2'), listpol('c^3'))))
print('a^3b^2 * 3a^2c^3 = '+ str(molt(listpol('a^3b^2'), listpol('a^2c^3'))))
print('x^2y^3 * x^3m^2 = '+ str(molt(listpol('x^2y^3'), listpol('x^3m^2'))))
print('p^4q^5 * p^3r^4   = '+ str(molt(listpol('p^4q^5'), listpol('p^3r^4'))))

