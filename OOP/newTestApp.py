from listpol import listpol
from monomio import Monomio
from mathTools import *
from polinomio import Polinomio

dimensione = int(input("inserire quanti monomi avrà il polinomio"))
arrs=[]
for i in range (dimensione):
    t = str(input("inserire monomio " +  str(i)))
    arrs.append(convertiDaStringaAOggetto(listpol(t)))
    
pol1 = Polinomio(arrs)
#print(pol1)

dimensione = int(input("inserire quanti monomi avrà il polinomio"))
arrs=[]
for i in range (dimensione):
    t = str(input("inserire monomio " +  str(i)))
    arrs.append(convertiDaStringaAOggetto(listpol(t)))

pol2 = Polinomio(arrs)

print(moltiplica2soliPolinomi(pol1, pol2))