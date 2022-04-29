#Aplicação

import listinha
import cone

tamanho=int(input("digite o tamanho da lista:"))
lista = listinha.Listinha(tamanho)


opc=5
while opc != 9:
    opc=int(input("\n1-insere 2-remove 3-exibe lista 9-fim \nSelecione:"))
    if opc == 1:

        if lista.listaCheia():
            print("lista cheia")
        else:
            raio = int(input("Digite o raio:"))
            altura = int(input("Digite a altura:"))
            x=cone.Cone(raio,altura)
            lista.insere(x)
            print("inserção com sucesso!!!")

    elif opc == 2:
        if lista.listaVazia():
            print("A lista está vazia!")
        else:
            lista.remove()
            print("removido!")

    elif opc == 3:
        if lista.listaVazia():
            print("A lista está vazia!")
        else:
            for i in range(lista.getTamanhoAtual()):
                x=lista.getValor(i)
                print("\nDados do Cone")
                print("\nAltura: ",x.getAltura())
                print("Raio: ",x.getRaio())
                print("Volume: ",x.getVolume())

    elif opc == 9:
        print("fim...")
    else:
        print("opção inválida!")
