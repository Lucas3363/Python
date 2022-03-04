#definindo um triangulo

class Triangulo:

    def __init__(self,altura,base,ladoA,ladoB,ladoC):
        self.altura = altura
        self.base = base
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def getArea(self):
        return (self.base*self.altura)/2

    def getPerimetro(self):
        return self.ladoA + self.ladoB + self.ladoC

    def getBase(self):
        return self.base
    
    def getAltura(self):
        return self.altura

    def getA(self):
        return self.ladoA

    def getB(self):
        return self.ladoB

    def getC(self):
        return self.ladoC   