import arcondicionado

temperatura = arcondicionado.Temperatura()

opc=0

while opc != 9:
    tempatual = temperatura.get_Temperatura()
    print(f"Temperatura atual: {tempatual}")

    opc=int(input("1- Aumenta 1 grau \n2- Diminui 1 grau. \n9- Desliga o ar. \nAperte um botão: "))
    if opc == 1 and temperatura.get_Temperatura()<26:
        temperatura.setAdd()
    elif opc==2 and temperatura.get_Temperatura()>17:
        temperatura.setLow()
    elif tempatual == 26:
        print("\nTemperatura máxima atingida")
    elif tempatual == 17:
        print("\nTemperatura mínima atingida")
    elif opc==9:
        print("PIIIII - Ar condicionado desligado")
    else:
        print("opção inválida")