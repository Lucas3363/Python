

class Fila:

    def __init__(self, tam=10):
        self.tamanho=tam
        self.fila=[]

    def insere(self, x):
        self.fila.append(x)

    def remover(self):
        self.fila.pop()

    def primeiros(self):
        return self.fila[0]

    def filaVazia(self):
        return len(self.fila) == 0

    def filaCheia(self):
        return len(self.fila) == self.tamanho

    def getFila(self):
        return self.fila