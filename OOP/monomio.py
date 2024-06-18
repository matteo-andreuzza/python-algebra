class Monomio:
    def __init__(self, variabili, coefficente):
        self.variabili = variabili
        self.coefficente = coefficente
        
    def getParteLetterale(self):
        return self.variabili
    def getCoefficente(self):
        return self.coefficente
    def toString(self):
        parteletterale = ""
        for variabiliPar in self.variabili:
            if self.variabili[variabiliPar] != 1:
                parteletterale += variabiliPar
                parteletterale += "^"
                parteletterale += str(self.variabili[variabiliPar])
            else:
                parteletterale += variabiliPar
        return str(self.coefficente) + parteletterale