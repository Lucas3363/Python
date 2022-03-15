import pilhasequencial

tamanho = int(input("Digite o tamanho da pilha:"))
p=pilhasequencial.Pilha(tamanho)

opc=1
while(opc != 9):
    opc=int(input("1-empilha 2-desempilha 3-topo 4-exibe Selecine:"))
    if opc==1:
        if p.pilhacheia():
            print("Pilha cheia!!")
        else:
            x=int(input("digite o valor: "))
            p.empilha(x)
            print("Sucesso")
    elif opc == 2:
        if p.pilhavazia():
            print("Pilha vazia....")
        else:
            p.desempilha()
            print("Desempilhado")
    elif opc == 3:
        if p.pilhavazia():
            print("Pilha vazia....")
        else:
            print("Topo da Pilha:", p.elementodotopo())
    elif opc == 4:
        if p.pilhavazia():
            print("Pilha vazia....")
        else:
            print("elementos da pilha: ",end="")
            for e in p.getPilha():
                print(e, end=" ")
            print()
    elif opc == 9:
        print("fim....")
    else:
        print("opção inválida")
        
        
        
        



