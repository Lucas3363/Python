from re import X


class Fila:

    def __init__(self, tam=10):
        self.tamanho=tam
        self.fila=[]

    def insereInicio(self, x):
        self.fila.append(x)

    def insereFinal(self, y):
        self.fila.insert(0, y)

    def removeFinal(self):
        self.fila.pop()

    def removeInicio(self):
        self.fila.pop(0)

    def exibePrimeiro(self):
        return self.fila[0]

    def exibeUltimo(self):
        return self.fila[-1]

    # def ultimo(self):
    #     return self.fila[len(self.fila)-1]

    def filaVazia(self):
        return len(self.fila) == 0

    def filaCheia(self):
        return len(self.fila) == self.tamanho

    def getFila(self):
        return self.fila
    
