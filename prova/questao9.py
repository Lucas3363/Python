menu = ('''
    \nSelecione uma opção:

    1 - Converter número para binário
    9 - finalizar programa
''')

opc = 1
while opc != 9:
    print(menu)
    opc = int(input())
    if opc == 1:
        temp = int(input('Digite um número: '))
        binario = bin(temp)
        print('\n', binario[2::])
    elif opc == 9:
        print("Programa finalizado!")    