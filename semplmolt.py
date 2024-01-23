# accetta polinomi STRINGA originati da polmolt e li converte in formato 
# pronto per algsum SENZA SEGNO +
# chiama inoltre aglsum nuovo e ritorna il risultato
#36x^2-60x^2+12x^2-20x^2

#TODO controllare variabili per usare algsum altrimenti dà errore

op = ['-', '+']
num = ['1','2','3','4','5','6','7','8','9']
lett = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from aggr import aggr
from main import algsum
from letpart import letpart
#36x^2-60x^2+12x^2-20x^2
def semplmolt(a):
    t = ['']
    c = 0
    i = 0
    t1 = 0
    k = []
    for i in a:
        t.append('')
    i = 0
    z = 0
    while i < len(a):
        z = 0
        try:
            while a[c] not in op:
                t[i] += a[c]
                c = c+1
                z = z+1
            if z != 0:
                i = i+z
                c = i
            else:
                t[i] += a[c]
                i = i + 1
                c = i
        except IndexError:
            break
    for i in t:
        if i == '':
            t.pop(t.index(i))
    for i in range(len(t)):
        try:
            if t[i] == '-':
                t1 = t[i]
                k=list(t[i+1])
                k.insert(0,t[i])
                t[i+1] = aggr(k, 's')
                t.pop(i)
        except IndexError:
            break
    x = len(t)
    i = 0
    while i < x:
        if t[i] == '' or t[i] == '+':
            t.pop(i)
            x = x-1
        else:
            i = i+1
    return t


print(semplmolt('36x^2-60x^2+12x^2-20x^2'))

#? semplifica polinomio usando semplmolt:
# print(sempl('36x^2-60x^2+12x-20x'))
# -24x^2-8x
# ( ['-24x^2', '-8x'] )

def sempl(a):
    a = semplmolt(a)
    g = 0
    flag = False
    t = []
    r = []
    z = []
    for i in a:
        if letpart(i) in t:
            continue
        else:
            t.append(letpart(i))
    for i in t:
        for k in a:
            if letpart(k) == i:
                r.append(k)
                r=algsum(r)
        z.append(aggr(r,'s'))
        r = []
        
    return aggr(z, 's')

print(sempl('36x^2-60x^2+12x-20x'))

print(sempl('36x^2-60x^2+12x^2-20x^2'))
