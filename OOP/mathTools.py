from monomio import Monomio
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
        if monomioInListaFormatoListpol[i+1] == '^':
            tempVariabili[monomioInListaFormatoListpol[i]] = monomioInListaFormatoListpol[i+2]
            i += 3
            
        else:
            tempVariabili[monomioInListaFormatoListpol[i]] = 1
            i+=1
        
    print("tempvariabili" + str(tempVariabili))
    print("tempCoefficente" + str(tempCoefficente))
    
    return Monomio(tempVariabili, int(tempCoefficente))
    
def sommaMonomi(monomioA, monomioB):
    if monomioA.variabili == monomioB.variabili:
        variabiliDaRitornare = monomioA.variabili
        coefficenteDaRitornare = monomioA.coefficente + monomioB.coefficente
        return Monomio(variabiliDaRitornare, coefficenteDaRitornare)
    else:
        return "errore, le parti letterali devono essere uguali"
