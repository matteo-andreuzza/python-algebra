from listpol import listpol
from newsum import newsum
a = ''
b = ''

"""def molt(x,y):
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
    return str(int(w)*int(q))+str(q2) + str(w2)"""
op = ['-', '+']
num = ['1','2','3','4','5','6','7','8','9']
lett = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import re

def fil(lista):
    # Utilizza la list comprehension e regex per filtrare numeri, lettere e espressioni alfanumeriche
    lista_filtrata = [elemento for elemento in lista if re.search(r'[a-zA-Z0-9]', str(elemento))]
    return lista_filtrata

def algsum(d): #! FUNZIONA, NON TOCCARE 
    fi = []    #? il 31/12/2023 con git siamo tornati alla versione precedente perchè per qualche motivo era stata modificata e resa inutilizzabile
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
            c[i] = newsum(t1,t2)
        except IndexError:
            t1 = c[i-1]
            t2 = c[i-2]
            c.pop(i-2)
            l = l-1
            c[i-2] = newsum(t1,t2)
    return c
        
        

print(algsum(['-5pq', '6pq', '-10pq'])) #! DA LASCIARE PER CONTINUO TESTING
print(algsum(['-5p^2', '6p^2', '-10p^2'])) #! non accetta letterali esponenziali
