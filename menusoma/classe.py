n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Segundo Valor: "))

opcao = 0
while opcao != 5:
    print('''
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior número
    [4] - Novos números
    [5] - Finalizar programa    
    ''')
    opcao = int(input("Qual é sua opção? "))
    if opcao == 1:
        soma = n1 + n2
        print("A soma entre {} + {} é {}".format(n1, n2, soma))

    elif opcao == 2:
        multi = n1 * n2
        print("A multiplicação entre {} x {} é {}".format(n1, n2, multi))

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("O maior número entre {} e {} é {}".format(n1, n2, maior))
        
    elif opcao == 4:
        n1 = int(input("Digite o novo primeiro número: "))
        n2 = int(input("Digite o novo segundo número: "))

    else:
        print("Digite uma opção entre 1 e 5 seu jumento")
    
    print("=-=" * 12)


print("\nFim do programa\n")