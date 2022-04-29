import prova1

tamanho = int(input("Digite o tamanho da fila: "))
f=prova1.Fila(tamanho)

opc=1
while opc != 9:
    opc = int(input("\n1 - Empilha  2 - Desempilha  3 - primeiro item da fila  4 - Exibe fila 5 - insere(remove()) 6 - insere(primeiro()) \nSelecione: "))
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

    elif opc == 5:
            f.insere(remover())
            print("insere(remove())")

    elif opc == 6:
            f.insere(primeiros())
            print("insere(primeiro())")
        
    elif opc == 9:
        print("Fim!")

else:
    print("Opção inválida!")
