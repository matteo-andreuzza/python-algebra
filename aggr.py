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
        if a[k+1] == '^':
            t.append(a[k] + a[k+1] + a[k+2])
            k = k +2
        else:
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
