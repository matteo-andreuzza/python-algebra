from monomio import Monomio
from listpol import listpol
def convertiDaStringaAOggetto(monomioInListaFormatoListpol):
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

def moltipolicaMonomi(monomioA, monomioB):
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
    return Monomio(variabiliDaRitornare, cofficenteDaRitornare)

print(moltipolicaMonomi(convertiDaStringaAOggetto(listpol("2a^2")),convertiDaStringaAOggetto(listpol("2xy"))).toString())