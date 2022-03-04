#definindo um triangulo

class Triangulo:

    def __init__(self,altura,base,lado3):
        self.altura = altura
        self.base = base
        self.lado3 = lado3

    def getArea(self):
        return (self.base*self.altura)/2

    def getPerimetro(self):
        return self.base+self.altura+self.lado3

    def getBase(self):
        return self.base
    
    def getAltura(self):
        return self.altura

    def getC(self):
        return self.lado3