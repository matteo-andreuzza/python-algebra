# aggrega una lista di termini esponenziali passati come parametro formattata in 
# formato listpol:
#['a^5', 'b', '^', '2', 'c', '^', '3']
# diventa:
#['a^5', 'b^2', 'c^3']
from listpol import listpol

def aggr(a,s):
    t = []
    g = ''
    k = 0
    while k < len(a): # scorre lista
        try:
            if a[k+1] == '^':
                t.append(a[k] + a[k+1] + a[k+2])
                k = k +2
            else:
                t.append(a[k])
        except IndexError:
            t.append(a[k])
            
        k = k+1
    if s == 's': # ritorno stringa
        for i in t:
            g += i
        return g
    elif s == 'a': # ritorno array
        return t
    else:
        return "errore parametro s"

def tostring(array):
    s = ''
    for i in array:
        s+=i
    return s

print(tostring(['40cd', '20c^2', '-10cb', '-32bd', '-16bc', '8b^2', '24ad', '12ac', '-6ab']))

print(aggr(['a^5', 'b', '^', '2', 'c', '^', '3','4', 'z', 'x'],'a'))