'''
4.	Para cadastrar os DVDs de uma pessoa amante da música, optou-se por utilizar um dicionário na linguagem Python. Escreva o programa para uma lista de Álbuns Musicais identificados pelo título do álbum e o musica das músicas pertencentes a esse álbum. Para isto, crie um menu da aplicação com as seguintes atividades:
'''
dic_cadastro   = {}
dic_musica = {}

menu = ('''
    \nSelecione uma opção:

    1-cadastrar um álbum 
    2-alterar o musica de uma música de um álbum 
    3-excluir um álbum
    4-listar os álbuns e suas músicas
    9-fim

''')

opc = 5
while opc != 9:
    print(menu)
    opc = int(input())
    #Cadastrar
    if opc == 1:
        album = str(input("\nDigite o album: "))
        if dic_cadastro.get(album):
            print("Album já cadastrado.")
        else:
            musica       = str(input("Digite seu musica: "))
            dic_cadastro.update({album: {"musica":musica}})
            if len(dic_musica) == 0:
                dic_musica.update({1:album})
            else: 
                for chave, valor in dic_musica.items():
                    dic_musica.update({chave+1:album})
                    break
            print("Cadastrado!")
    #Alterar
    elif opc == 2:
        if len(dic_cadastro) == 0:
            print("Lista vazia.")
        else:
            album = str(input("Digite o album: "))
            if dic_cadastro.get(album):
                musica       = str(input("Digite a musica: "))
                dic_cadastro[album] = {"musica":musica}
                print("Atualizado!")
            else:
                print("album não cadastrado.")
    #Excluir
    elif opc == 3:
        if len(dic_cadastro) == 0:
            print("Lista vazia.")
        else:
            album = str(input("Digite o nome do album: "))
            if dic_cadastro.get(album):
                del dic_cadastro[album]
                for chave, valor in dic_musica.items():
                    if valor == album:
                        del dic_musica[chave]
                        break
                print("Excluído!")
            else:
                print("album não cadastrado.")
    #Listar
    elif opc == 4:
        if len(dic_cadastro) == 0:
            print("Lista vazia.")
        else:
            for chave, valor in dic_musica.items():
                print(f"\nalbum: {valor}\nmusica:     {dic_cadastro[valor]['musica']}")
                print("\n============================")
    #Resto
    elif opc == 9:
        print("Programa finalizado!")
    else: 
        print("Opção inválida!")
    print()