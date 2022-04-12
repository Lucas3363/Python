class Cadastro:

    def __init__(self, tam=10):
        self.tamanho=tam
        self.cadastro={}

    def insere(self):
        self.cadastro.append()

    def removeItem(self, x):
        self.cadastro.pop(x)

    def cadastroVazio(self):
        return len(self.cadastro) == 0

    def cadastroCheio(self):
        return len(self.cadastro) == self.tamanho

    def getFila(self):
        return self.cadastro