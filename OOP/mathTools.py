from monomio import Monomio
from listpol import listpol
from polinomio import Polinomio
import copy
def convertiDaStringaAOggetto(monomioInListaFormatoListpol):
    if str in monomioInListaFormatoListpol:
        return convertiDaStringaAOggetto(monomioInListaFormatoListpol)
    else:
        return convertiDaStringaAOggetto(listpol(str(monomioInListaFormatoListpol.append("&"))))
    tempCoefficente = ''
    tempVariabili = {}
    for i in range(len(monomioInListaFormatoListpol)):
        try:
            while monomioInListaFormatoListpol[i] == "-"  or type(int(monomioInListaFormatoListpol[i])) == int :
                tempCoefficente += monomioInListaFormatoListpol[i]
                monomioInListaFormatoListpol.pop(i)
        except ValueError:
            if(tempCoefficente == 0):
                tempCoefficente = 1
            break
        
    i = 0    
    while i < len(monomioInListaFormatoListpol):
        try:
            if monomioInListaFormatoListpol[i+1] == '^':
                tempVariabili[monomioInListaFormatoListpol[i]] = monomioInListaFormatoListpol[i+2]
                i += 3
                
            else:
                tempVariabili[monomioInListaFormatoListpol[i]] = 1
                i+=1
        except IndexError:
            tempVariabili[monomioInListaFormatoListpol[i]] = 1
            i+=1
        
    print("tempvariabili" + str(tempVariabili))
    print("tempCoefficente" + str(tempCoefficente))
    
    return Monomio(tempVariabili, int(tempCoefficente))
    
def sommaMonomi(monomioA, monomioB):
    #TODO se errore, restituisce un polinomio
    if monomioA.variabili == monomioB.variabili:
        variabiliDaRitornare = monomioA.variabili
        coefficenteDaRitornare = monomioA.coefficente + monomioB.coefficente
        return Monomio(variabiliDaRitornare, coefficenteDaRitornare)
    else:
        return "errore, le parti letterali devono essere uguali"

def moltipolicaMonomi(monomioAPar, monomioBPar):
    monomioA = copy.deepcopy(monomioAPar)
    monomioB = copy.deepcopy(monomioBPar)
    if len(monomioA.getParteLetterale()) > len(monomioB.getParteLetterale()):
        return moltipolicaMonomi(monomioB, monomioA)
    variabiliDaRitornare = {}
    cofficenteDaRitornare = monomioA.getCoefficente() * monomioB.getCoefficente()
    for variabili in monomioA.variabili.copy():#! uso .copy perché la dimensione del dizionario cambia durante l'iterazion
        for variabili2 in monomioB.variabili.copy(): #! altrimenti RuntimeError
            if variabili == variabili2:
                variabiliDaRitornare[variabili]=str(int(monomioA.variabili[variabili2]) + int(monomioB.variabili[variabili2])) #converto al volo altrimenti somma come stringhe gli espnenti
                monomioA.variabili.pop(variabili)
                monomioB.variabili.pop(variabili2)
            else:
                try:
                    variabiliDaRitornare[variabili] = monomioA.variabili.copy()[variabili]
                    monomioA.variabili.pop(variabili)
                    variabiliDaRitornare[variabili2] = monomioB.variabili[variabili2]
                    monomioB.variabili.pop(variabili2)
                except KeyError:
                    for variabile in monomioB.variabili.copy():
                        variabiliDaRitornare[variabile] = monomioB.variabili[variabile]
    if '&' in variabiliDaRitornare:
        variabiliDaRitornare.pop('&')
        return Monomio(variabiliDaRitornare, cofficenteDaRitornare)
    else:
        return Monomio(variabiliDaRitornare, cofficenteDaRitornare)

#TEST print(moltipolicaMonomi(convertiDaStringaAOggetto(listpol("2a^2b^2")),convertiDaStringaAOggetto(listpol("2xy"))).toString())

def moltiplicaPolinomi(polinomioA, polinomioB):
    arrMonomiDaRitornare = []
    for monomi in polinomioA.arrMonomi:
        for monomio in polinomioB.arrMonomi:
            arrMonomiDaRitornare.append(moltipolicaMonomi(monomi, monomio).toString())
    return str(arrMonomiDaRitornare)

#print(moltiplicaPolinomi(Polinomio([Monomio({'a':2}, 2), Monomio({'a':3}, 2)]),Polinomio([Monomio({'a':2}, 2), Monomio({'b':3}, 2)])))
#print(moltiplicaPolinomi(Polinomio([Monomio({'x':2}, 1), Monomio({'x':1}, -2)]),Polinomio([Monomio({'a':2}, 2), Monomio({'b':1}, -2)])))


print(moltipolicaMonomi(convertiDaStringaAOggetto(listpol("2&")), convertiDaStringaAOggetto(listpol("4a"))).toString())