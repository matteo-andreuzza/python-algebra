# moltiplicazione di polinomi SENZA PASSARE I SEGNI
# accetta in formato array:
# print(polmolt(['a^2b^2'], ['a^2c', '2ac']))

from newmolt import algmolt
from listpol import listpol
from aggr import aggr
def polmolt(a,b):
    print(f""" 
****** MOLTIPLICAZIONE  ****
DI   {aggr(a,'s')} * {str(b)}
    """)
      
    t = []
    for i in range(len(a)):
        for k in range(len(b)):
            t.append(algmolt(listpol(a[i]),listpol(b[k])))
    t = list(aggr(t,'s'))
    if t[0] == '+': #toglie segno dato da algmolt dal primo.
        t.pop(0)
    return aggr(t,'s')
            
print(polmolt(['a^2b^2'], ['a^2c', '2ac']))
print(polmolt(['12x','4x'], ['3x', '-5x']))