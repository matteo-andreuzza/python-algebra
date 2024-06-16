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
        for variabili in self.variabili:
            parteletterale += variabili
            parteletterale += "^"
            parteletterale += self.variabili[variabili]
        return str(self.coefficente) + parteletterale