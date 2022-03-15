from re import X


class Fila:

    def __init__(self, tam=10):
        self.tamanho=tam
        self.fila=[]

    def insere(self, x):
        self.fila.append(x)

    def remove(self):
        self.fila.pop()

    def primeiro(self):
        return self.fila[0]

    def filaVazia(self):
        return len(self.fila) == 0

    def filaCheia(self):
        return len(self.fila) == self.tamanho

    def getFila(self):
        return self.fila
    
