# creo un nuovo monomio da input utente e restituisco i valori
from listpol import listpol
from monomio import Monomio
from mathTools import *
from polinomio import Polinomio
monomioPar = input("inserire monomio ")

monomio = convertiDaStringaAOggetto(listpol(monomioPar))

#stampo attributi

print("parte letterale del monomio " + str(monomio.getParteLetterale()))
print("coefficente del monomio " + str(monomio.getCoefficente()))

monomioPar1 = input("inserire monomio ")

monomio1 = convertiDaStringaAOggetto(listpol(monomioPar1))

#stampo attributi

print("parte letterale del monomio " + str(monomio1.getParteLetterale()))
print("coefficente del monomio " + str(monomio1.getCoefficente()))

#somma = sommaMonomi(monomio1, monomio)


#print("parte letterale del monomio somma " + str(somma.getParteLetterale()))
#print("coefficente del monomio somma " + str(somma.getCoefficente()))
#print("parte letterale stringa " + somma.toString())

print("PRODOTTO DEI DUE MONOMI")
prodotto = moltipolicaMonomi(monomio1, monomio)


print("parte letterale del monomio prodotto " + str(prodotto.getParteLetterale()))
print("coefficente del monomio prodotto " + str(prodotto.getCoefficente()))
print("stringa " + prodotto.toString())

print("####")
print("####")
print("####")
print("####")
print("creo polinomi")
pol = Polinomio([monomio1, monomio])
print(pol)
pol2 = Polinomio([monomio, prodotto])
print(pol2)
print("prdotto polinomoni " + moltiplica2soliPolinomi(pol, pol2))