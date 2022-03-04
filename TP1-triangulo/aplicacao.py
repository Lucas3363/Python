#Aplicação

import listinha
import triangulo

tamanho=int(input("digite o tamanho da lista:"))
lista = listinha.Listinha(tamanho)


opc=5
while opc != 9:
    opc=int(input("\n1-insere 2-remove 3-exibe lista 9-fim \nSelecione:"))
    if opc == 1:

        if lista.listaCheia():
            print("lista cheia")
        else:
            base = int(input("Digite a base:"))
            altura = int(input("Digite a altura:"))
            ladoA = int(input("Digite o lado A: "))
            ladoB = int(input("Digite o lado B: "))
            ladoC = int(input("Digite o lado C: "))
            x=triangulo.Triangulo(base,altura,ladoA,ladoB,ladoC)
            lista.insere(x)
            print("inserção com sucesso!!!")

    elif opc == 2:
        if lista.listaVazia():
            print("A list está vazia!")
        else:
            lista.remove()
            print("removido!")

    elif opc == 3:
        if lista.listaVazia():
            print("A list está vazia!")
        else:
            for i in range(lista.getTamanhoAtual()):
                x=lista.getValor(i)
                print("\nDados do triangulo")
                print("\nLado A: ",x.getA())
                print("Lado B: ",x.getB())
                print("Lado C: ",x.getC())
                print("\nArea:",x.getArea())
                print("Perimetro:",x.getPerimetro())

    elif opc == 9:
        print("fim...")
    else:
        print("opção inválida!")
