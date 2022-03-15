'''
1 - venda  //vende um ingresso indicando qual posição a pessoa deseja ocupar
2 - devolução //permite à pessoa que devolva o ingresso que tinha comprado.
3 - exibe  //Exibe da situação atual do teatro: Lugares ocupados, livres e quantidade vendida.
9 - fim de execução.
'''

import classeMatriz
import contador_v2


linha =int(input("Digite a quantidade de fileiras: ")) 
coluna = int(input("Digite a quantidade de poltronas por cada fileira: ")) 
teatro = classeMatriz.Matriz(linha,coluna)


valormax = linha*coluna
valor=0
cont = contador_v2.Contador(valor,valormax)

opc=0
while opc != 9:    
    
    for i in range(teatro.getLin()):
        for j in range(teatro.getCol()):
            print(teatro.getValor(i,j),end="  ")
        print()
    
    print("\n1 - Venda de ingresso")
    print("2 - devolução de ingresso")
    print("3 - Exibir as poltronas ocupadas")
    print("9 - fim")
    
    opc=int(input("\nSelecione: "))
    if opc == 1:
        linha= int(input("Fileira que deseja ocupar:"))
        coluna= int(input("Poltrona na fileira que deseja ocupar:"))
        x=classeMatriz.Matriz(linha,coluna)
        if linha < teatro.getLin() and coluna < teatro.getCol():
            if teatro.getOcupada(linha,coluna)==True:
                teatro.insere(linha,coluna,"x")                
                cont.set_Inc()
            else:
                print("Cadeira ocupada!") 
        else:
            print("Cadeira não existente!")
        
            
    elif opc == 2:
        for i in range(teatro.getLin()):
            for j in range(teatro.getCol()):
                print(teatro.getValor(i,j),end="  ")
            print()
        linha= int(input("Fileira que deseja desocupar:"))
        coluna= int(input("Poltrona na fileira que deseja desocupar:"))
        x=classeMatriz.Matriz(linha,coluna)
        if linha < teatro.getLin() and coluna < teatro.getCol():
            if teatro.getOcupada(linha,coluna)==False:
                teatro.devolve(linha,coluna)
        cont.set_Dec()
        print("Devolvido!")
        
    elif opc == 3:        
        for i in range(teatro.getLin()):
            for j in range(teatro.getCol()):
                print(teatro.getValor(i,j),end="  ")
            print()

        print("\nPoltronas ocupadas:",cont.getContador(valor,valormax))
        print("Poltronas vendidas:",cont.getContador(valor,valormax))      
        print("Poltronas livres:",cont.getLivres(valor,valormax))
    elif opc == 9:
        print("fim....")
    else:
        print("opção inválida!!")
    

    
