from tkinter import Y
import classefila

tamanho = int(input("Digite o tamanho da fila: "))
f=classefila.Fila(tamanho)

opc=1
while opc != 9:
    opc = int(input("\n1 - Empilha  2 - Adicionar no inicio  3 - Remover primeiro número  4 - Remover ultimo número  \n5 - primeiro item da fila  6 - Ultimo item da lista  7 - Exibe fila  8 - Sair \nSelecione: "))
    if opc == 1:
        if f.filaCheia():
            print("\nFila cheia!")
        else:
            x = int(input("Digite o valor para adicionar a fila: "))
            f.insere(x)
            print("\nInserido!")

    elif opc == 2:
        if f.filaCheia():
            print("\nLista cheiaaaa!!!!")
        else:
            y = int(input("Digite o valor para adicionar no INICIO da fila: "))
            f.insereFinal(y)
            print("\nInserido no inicio!")
    
    elif opc == 3:
        if f.filaVazia():
            print("\nFila vazia!")
        else:
            f.removeInicio()
            print("\nRemovido!")

    elif opc == 4:
        if f.filaVazia():
            print("\nFila vazia!")
        else:
            f.remove()
            print("\nRemovido!")

    elif opc == 5:
        if f.filaVazia():
            print("\nFila vazia!")
        else:
            print("\nO primeiro item é: ", f.primeiro())

    elif opc == 6:
        if f.filaVazia():
            print("Lista vazia meu!")
        else:
            print("\nO ultimo item é: ", f.ultimo())
    
    elif opc == 7:
        if f.filaVazia():
            print("\nFila vazia!")
        else:
            print("\nExibindo fila:", f.getFila())
        
    elif opc == 8:
        print("\nFim!")

else:
    print("\nOpção inválida!")
