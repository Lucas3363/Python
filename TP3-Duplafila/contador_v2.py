class Contador:
    
    def __init__(self,valor,valormax):
        self.contador = valor
        self.max = valormax

    def set_Inc(self):
        if self.contador < self.max:
            self.contador+=1

    def set_Dec(self):
        self.contador-=1

    def getContador(self,valor,valormax):
        return self.contador

    def getLivres(self,valor,valormax):
        return self.max - self.contador
    
    

















        


