import classefila

tamanho = int(input("Digite o tamanho da fila: "))
f=classefila.Fila(tamanho)

opc=1
while opc != 9:
    opc = int(input("\n1 - Empilha  2 - Desempilha  3 - primeiro item da fila  4 - Exibe fila \nSelecione: "))
    if opc == 1:
        if f.filaCheia():
            print("Fila cheia!")
        else:
            x = int(input("Digite o valor para adicionar a fila: "))
            f.insere(x)
            print("Inserido!")
    
    elif opc == 2:
        if f.filaVazia():
            print("Fila vazia!")
        else:
            f.remove()
            print("Removido!")

    elif opc == 3:
        if f.filaVazia():
            print("Fila vazia!")
        else:
            print(f.primeiro())
    
    elif opc == 4:
        if f.filaVazia():
            print("Fila vazia!")
        else:
            print("Exibindo fila:", f.getFila())
        
    elif opc == 9:
        print("Fim!")

else:
    print("Opção inválida!")
