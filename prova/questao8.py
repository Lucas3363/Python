dic_cadastro   = {}
dic_nome = {}

menu = ('''
    \nSelecione uma opção:

    1 - Cadastrar
    2 - Listar
    9 - Finalizar Programa
''')

opc = 5
while opc != 9:
    print(menu)
    opc = int(input())
    if opc == 1:
        nomegeral = str(input("\nDigite sua matrícula: "))
        if dic_cadastro.get(nomegeral):
            print("Aluno já cadastrado.")
        else:
            nome       = str(input("\nDigite seu nome: "))
            matricula   = str(input("Digite seu número de matrícula: "))
            ano     = str(input("Digite o ano que o aluno estuda: "))
            semestre     = str(input("Digite o semestre que o aluno estuda: "))
            nota1     = str(input("Digite a primeira nota: "))
            nota2     = str(input("Digite a segunda nota: "))
            dic_cadastro.update({nomegeral: {"Nome":nome, "Matrícula":matricula, "Ano":ano, "Semestre":semestre, "Nota 1":nota1, "Nota 2":nota2}})
            if len(dic_nome) == 0:
                dic_nome.update({1:nomegeral})
            else: 
                for chave, valor in dic_nome.items():
                    dic_nome.update({chave+1:nomegeral})
                    break
            print("Cadastrado!")
    elif opc == 2:
        if len(dic_cadastro) == 0:
            print("Lista vazia.")
        else:
            for chave, valor in dic_nome.items():
                print(f"\nNome: {dic_cadastro[valor]['Nome']}\nMatrícula:     {dic_cadastro[valor]['Matrícula']}\nAno: {dic_cadastro[valor]['Ano']}\nSemestre:   {dic_cadastro[valor]['Semestre']}\nNota 1:   {dic_cadastro[valor]['Nota 1']}\nNota 2:   {dic_cadastro[valor]['Nota 2']}")
                print("\n============================")
    elif opc == 9:
        print("Programa finalizado!")
    else: 
        print("Opção inválida!")
    print()