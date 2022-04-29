class Listinha:

#elementos da classe

    def __init__(self,tam=10):
        self.lista=[]
        self.tamanho = tam
    
#lógica das operações

    def insere(self,x):
        self.lista.append(x)

    def remove(self):
        self.lista.pop()

    def getValor(self,indice):
        return self.lista[indice]

    def getTamanhoAtual(self):
        return len(self.lista)

    def listaCheia(self):
        return len(self.lista) == self.tamanho

    def listaVazia(self):
        return len(self.lista) == 0