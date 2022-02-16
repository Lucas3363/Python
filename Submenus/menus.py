filmes = []
categoria = []


def menu(titulo, opcoes):
    while True:
        print("=" * len(titulo), titulo, "=" * len(titulo), sep="\n")
        for i, (opcao, funcao) in enumerate(opcoes, 1):
            print("[{}] - {}".format(i, opcao))
        print("[{}] - Retornar/Sair".format(i+1))
        op = input("Opção: ")
        if op.isdigit():
            if int(op) == i + 1:
                # Encerra este menu e retorna a função anterior
                break
            if int(op) < len(opcoes):
                # Chama a função do menu:
                opcoes[int(op) - 1][1]()
                continue
        print("Opção inválida. \n\n")

def principal():
    opcoes = [
        ("Adicionar", adicionar),
        ("Listar", listar),
        ("Procurar", procurar)
    ]
    return menu("FILMES", opcoes)

def adicionar():
    opcoes = [
        ("FILMES", adicionar_filme),
        ("CATEGORIAS", adicionar_categoria),
        # ...
    ]
    return menu("Adicionar", opcoes)

def adicionar_filme():
    filmes.append(input("Novo filme: "))


def adicionar_categoria():
    categoria.append(input("Nova categoria: "))

    #...

def listar():
   return filmes

def procurar():
    return categoria

principal()