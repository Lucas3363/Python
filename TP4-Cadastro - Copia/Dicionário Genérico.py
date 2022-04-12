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
dic_cad   = {}
dic_n_tel = {}

menu = ('''============================
    Selecione uma opção:
============================
    [1] Cadastrar
    [2] Pesquisar
    [3] Alterar
    [4] Excluir
    [5] Listar
    [9] Finalizar Programa
============================''')

opc = 5
while opc != 9:
    print(menu)
    opc = int(input())
    #Cadastrar
    if opc == 1:
        n_tel = str(input("Digite seu número de telefone: "))
        if dic_cad.get(n_tel):
            print("Telefone já cadastrado.")
        else:
            nome       = str(input("Digite seu nome: "))
            endereco   = str(input("Digite seu endereço: "))
            cidade     = str(input("Digite o nome da cidade onde mora: "))
            estado     = str(input("Digite o nome da estado onde mora: "))
            dic_cad.update({n_tel: {"Nome":nome, "Endereço":endereco, "Cidade":cidade, "Estado":estado}})
            if len(dic_n_tel) == 0:
                dic_n_tel.update({1:n_tel})
            else: 
                for chave, valor in dic_n_tel.items():
                    dic_n_tel.update({chave+1:n_tel})
                    break
            print("Cadastrado!")
    #Pesquisar
    elif opc == 2:
        if len(dic_cad) == 0:
            print("Lista vazia.")
        else:
            n_tel = str(input("Digite seu número de telefone: "))
            if dic_cad.get(n_tel):
                print(f"Nome:     {dic_cad[n_tel]['Nome']}\nEndereço: {dic_cad[n_tel]['Endereço']}\nCidade:   {dic_cad[n_tel]['Cidade']}\nEstado:   {dic_cad[n_tel]['Estado']}")
            else:
                print("Telefone não cadastrado.")
    #Alterar
    elif opc == 3:
        if len(dic_cad) == 0:
            print("Lista vazia.")
        else:
            n_tel = str(input("Digite seu número de telefone: "))
            if dic_cad.get(n_tel):
                nome       = str(input("Digite seu nome: "))
                endereco   = str(input("Digite seu endereço: "))
                cidade     = str(input("Digite o nome da cidade onde mora: "))
                estado     = str(input("Digite o nome da estado onde mora: "))
                dic_cad[n_tel] = {"Nome":nome, "Endereço":endereco, "Cidade":cidade, "Estado":estado}
                print("Atualizado!")
            else:
                print("Telefone não cadastrado.")
    #Excluir
    elif opc == 4:
        if len(dic_cad) == 0:
            print("Lista vazia.")
        else:
            n_tel = str(input("Digite seu número de telefone: "))
            if dic_cad.get(n_tel):
                del dic_cad[n_tel]
                for chave, valor in dic_n_tel.items():
                    if valor == n_tel:
                        del dic_n_tel[chave]
                        break
                print("Excluído!")
            else:
                print("Telefone não cadastrado.")
    #Listar
    elif opc == 5:
        if len(dic_cad) == 0:
            print("Lista vazia.")
        else:
            for chave, valor in dic_n_tel.items():
                print(f"Telefone: {valor}\nNome:     {dic_cad[valor]['Nome']}\nEndereço: {dic_cad[valor]['Endereço']}\nCidade:   {dic_cad[valor]['Cidade']}\nEstado:   {dic_cad[valor]['Estado']}")
                print("============================")
    #Resto
    elif opc == 9:
        print("Programa finalizado!")
    else: 
        print("Opção inválida!")
    print()