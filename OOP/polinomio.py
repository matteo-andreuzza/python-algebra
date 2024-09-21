class Polinomio:
    def __init__(self, arrMonomi):
        self.arrMonomi = arrMonomi
    def __str__(self):
        st = ""
        st += "["
        for monomio in self.arrMonomi:
            st += monomio.toString()
            
        st += "]"
        
        return st