class Matriz:
    def __init__(self,linha,coluna):
        self.lin=linha
        self.col=coluna
        self.m=[]
        for ln in range(self.lin): #construindo o numero de colunas
            lista=[]
            for cl in range(self.col):
                lista.append("0") #preenchendo a matriz com 0
            self.m.append(lista) #atribuindo a lista á matriz
            
    def insere(self,lin,col,x):
        self.m[lin][col]= "x"

    def devolve(self,lin,col):
        self.m[lin][col] = "0"
        
    def getLin(self):
        return self.lin
    
    def getCol(self):
        return self.col
    
    def getMatriz(self):
        return self.m

    def getValor(self,lin,col):
        return self.m[lin][col]

    def getOcupada(self,lin,col):
        return self.m[lin][col] == "0"
