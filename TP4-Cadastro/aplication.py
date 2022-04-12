import classecadastro

tamanho = int(input("Digite o número de cadastrados"))
f=classecadastro.Cadastro(tamanho)


opc=1
while opc != 9:
    opc = int(input("\n1 - Cadastrar telefone  2 - Pesquisar  3 - Alterar  4 - Excluir  \n5 - Listar tudo  9 - Sair \nSelecione: "))
    if opc == 1:
        if f.cadastroCheio():
            print("\nCadastro lotado!")
        elif int(input("Digite o telefone: ")):
            f.insere()
            print("Inserido!")
        elif int(input("Digite o nome da pessoa: ")):
            f.insereContato()
            print("Nome adicionado.")
        else:
            print("Opção inválida")

    elif opc == 2:
        if f.cadastroVazio():
            print("Lista de cadastro está vazia!")
        else:
            print
