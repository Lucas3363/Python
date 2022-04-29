#definindo um triangulo

class Cone:

    def __init__(self,altura,raio):
        self.altura = altura
        self.raio = raio
        self.pi = 3.14

    def getVolume(self):
        return (self.pi*self.raio*self.raio*self.altura)/3

    def getRaio(self):
        return self.raio
    
    def getAltura(self):
        return self.altura

