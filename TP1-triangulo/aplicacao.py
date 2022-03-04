#Aplicação

import listinha
import triangulo

tamanho=int(input("digite o tamanho da lista:"))
lista = listinha.Listinha(tamanho)


opc=5
while opc != 9:
    opc=int(input("1-insere 2-remove 3-exibe lista 9-fim \nSelecione:"))
    if opc == 1:

        if lista.listaCheia():
            print("lista cheia")
        else:
            base = int(input("Digite a base:"))
            altura = int(input("Digite a altura:"))
            lado3 = int(input("Digite o lado 3: "))
            x=triangulo.Triangulo(base,altura,lado3)
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
                print("Base:",x.getBase())
                print("Altura: ",x.getAltura())
                print("Lado 3: ",x.getC())
                print("Area:",x.getArea())
                print("Perimetro:",x.getPerimetro())

    elif opc == 9:
        print("fim...")
    else:
        print("opção inválida!")
