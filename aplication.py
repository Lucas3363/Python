import contador_v1

contador1 = contador_v1.Contador()

opc=0

while opc != 9:
    vc = contador1.get_Contador()
    print(f"valor atual: {vc}")

    opc=int(input("1-entrada 2-saida 9-fim \nSelecione:"))
    if opc == 1:
       contador1.setIncremento()
    elif opc==2 and contador1.get_Contador()>0:
        contador1.setDecremento()
    elif opc==9:
        print("fim...")
    else:
        print("opção inválida")