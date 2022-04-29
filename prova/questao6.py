import random

pilha = []
fila = []

menu = ('''
    \nSelecione uma opção:

    1 - preencher com numeros aleatorios.
    2 - exibir a fila
    3 - transferir da fila para a pilha
    4 - exibe fila
    9 - Finalizar programa.

    Opção:''')

opc = 4
while opc != 9:
    print(menu)
    opc = int(input())
    if opc == 1:
        for i in range(5):
            x = random.randint(35,75)
            fila.append(x)

    elif opc == 2:
        print('\n ', fila)

    elif opc == 3:
        pilha = fila

    elif opc == 4:
        print ('\n ', pilha)

    elif opc == 9:
        print('Programa finalizado!')

    else:
        print('Opção inválida.')
    print()