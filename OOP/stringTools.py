from polinomio import *
from monomio import *
from mathTools import *
from listpol import *
def detectAndCreatePolinomio(string):
    mon = []
    tr = []
    for i in range(len(string)):
        if string[i]!= "+":
            if string[i] == "-":
                i = i-1
                tr.append(mon)
                mon = []
                mon.append(string[i+1])
                continue
                
            mon.append(string[i])
        else:
            tr.append(mon)
            mon = []
            
    tr.append(mon)
    x= []
    for l in tr:
        x.append(''.join(l))
    
    return x

def createPolinomio(listDaDetectAndCreatePolinomio):
    arrMonomi = []
    toCreate = []
    for i in listDaDetectAndCreatePolinomio:
        arrMonomi.append(listpol(i))
    for z in arrMonomi:
        toCreate.append(convertiDaStringaAOggetto(z))
    return Polinomio(toCreate)
#print(listpol(detectAndCreatePolinomio("a^2b-2ab+b^2-2b+a^2b^3")))
#print(detectAndCreatePolinomio("2a^2+2b^3"))
#print(detectAndCreatePolinomio("7x^3-4x^2-x"))
                
#print(detectAndCreatePolinomio("2a-3z"))

import re

def aggiungi_coefficiente_1(polinomio: str) -> str:
    # Aggiunge uno spazio prima e dopo + e - per facilitare il parsing
    polinomio = re.sub(r'(?<!^)(?=[+-])', ' ', polinomio)

    monomi = polinomio.strip().split()
    monomi_modificati = []

    for monomio in monomi:
        if re.match(r'[a-zA-Z]', monomio):  # comincia con lettera
            monomi_modificati.append("1" + monomio)
        elif re.match(r'[+-][a-zA-Z]', monomio):  # comincia con +lettera o -lettera
            monomi_modificati.append(monomio[0] + "1" + monomio[1:])
        else:
            monomi_modificati.append(monomio)

    return ''.join(monomi_modificati)
print(createPolinomio(detectAndCreatePolinomio(aggiungi_coefficiente_1("a^2b-2ab+b^21-2b+a^2b^3"))))

def creaPolinomioDaStringa(stringa) -> Polinomio:
    return(createPolinomio(detectAndCreatePolinomio(aggiungi_coefficiente_1(stringa))))