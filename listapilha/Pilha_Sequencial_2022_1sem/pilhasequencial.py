

class Pilha:
    def __init__(self,tam=10):
        self.tamanho = tam
        self.pilha = []

    def empilha(self,x):
        self.pilha.append(x)

    def desempilha(self):
        self.pilha.pop()

    def elementodotopo(self):
        return self.pilha[len(self.pilha)-1]

    def pilhavazia(self):
        return len(self.pilha) == 0

    def pilhacheia(self):
        return len(self.pilha) == self.tamanho

    def getValor(posicao):
        return self.pilha[posicao]

    def getPilha(self):
        return self.pilha

        
    
    
