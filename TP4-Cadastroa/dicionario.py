'''
Escreve o programa Python para uma lista de pessoas identificadas pelo número de telefone, cujos dados são nome, endereço, cidade, estado.
Para isto, crie um menu da aplicação com as seguintes atividades:
1-cadastrar
2-pesquisar
3-alterar
4-excluir
5-listar (pode ser em ordem de nome?)
9-fim
'''
dic_cadastro   = {}
dic_n_telefone = {}

menu = ('''
    \nSelecione uma opção:

    1 - Cadastrar
    2 - Pesquisar
    3 - Alterar
    4 - Excluir
    5 - Listar
    9 - Finalizar Programa
''')

opc = 5
while opc != 9:
    print(menu)
    opc = int(input())
    #Cadastrar
    if opc == 1:
        n_tel = str(input("\nDigite seu número de telefone: "))
        if dic_cadastro.get(n_tel):
            print("Telefone já cadastrado.")
        else:
            nome       = str(input("Digite seu nome: "))
            endereco   = str(input("Digite seu endereço: "))
            cidade     = str(input("Digite o nome da cidade onde mora: "))
            estado     = str(input("Digite o nome da estado onde mora: "))
            dic_cadastro.update({n_tel: {"Nome":nome, "Endereço":endereco, "Cidade":cidade, "Estado":estado}})
            if len(dic_n_telefone) == 0:
                dic_n_telefone.update({1:n_tel})
            else: 
                for chave, valor in dic_n_telefone.items():
                    dic_n_telefone.update({chave+1:n_tel})
                    break
            print("Cadastrado!")
    #Pesquisar
    elif opc == 2:
        if len(dic_cadastro) == 0:
            print("Lista vazia.")
        else:
            n_tel = str(input("Digite seu número de telefone: "))
            if dic_cadastro.get(n_tel):
                print(f"Nome:     {dic_cadastro[n_tel]['Nome']}\nEndereço: {dic_cadastro[n_tel]['Endereço']}\nCidade:   {dic_cadastro[n_tel]['Cidade']}\nEstado:   {dic_cadastro[n_tel]['Estado']}")
            else:
                print("Telefone não cadastrado.")
    #Alterar
    elif opc == 3:
        if len(dic_cadastro) == 0:
            print("Lista vazia.")
        else:
            n_tel = str(input("Digite seu número de telefone: "))
            if dic_cadastro.get(n_tel):
                nome       = str(input("Digite seu nome: "))
                endereco   = str(input("Digite seu endereço: "))
                cidade     = str(input("Digite o nome da cidade onde mora: "))
                estado     = str(input("Digite o nome da estado onde mora: "))
                dic_cadastro[n_tel] = {"Nome":nome, "Endereço":endereco, "Cidade":cidade, "Estado":estado}
                print("Atualizado!")
            else:
                print("Telefone não cadastrado.")
    #Excluir
    elif opc == 4:
        if len(dic_cadastro) == 0:
            print("Lista vazia.")
        else:
            n_tel = str(input("Digite seu número de telefone: "))
            if dic_cadastro.get(n_tel):
                del dic_cadastro[n_tel]
                for chave, valor in dic_n_telefone.items():
                    if valor == n_tel:
                        del dic_n_telefone[chave]
                        break
                print("Excluído!")
            else:
                print("Telefone não cadastrado.")
    #Listar
    elif opc == 5:
        if len(dic_cadastro) == 0:
            print("Lista vazia.")
        else:
            for chave, valor in dic_n_telefone.items():
                print(f"\nTelefone: {valor}\nNome:     {dic_cadastro[valor]['Nome']}\nEndereço: {dic_cadastro[valor]['Endereço']}\nCidade:   {dic_cadastro[valor]['Cidade']}\nEstado:   {dic_cadastro[valor]['Estado']}")
                print("\n============================")
    #Resto
    elif opc == 9:
        print("Programa finalizado!")
    else: 
        print("Opção inválida!")
    print()