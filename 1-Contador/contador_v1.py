from ast import Return


1
# '''
# contador
# 1-entrada de pessoa
# 2-saida de pessoa
# 9-finalizar o programa

# exibir a situacao atual do contador
# '''

# #variável contadora de pessoas
# contador = 0
# #opção do usuário
# opc=0
# while opc != 9:
#     print(f"valor atual: {contador}")
#     opc=int(input("1-entrada 2-saida 9-fim \nSelecione:"))
#     if opc == 1:
#        contador+=1
#     elif opc==2 and contador>0:
#        contador-=1
#     elif opc==9:
#        print("fim...")
#     else:
#        print("opção inválida")

## VERSAO 2
## CONTADOR


class Contador:

   def __init__(self):
      self.contador = 0

   def setIncremento(self):
      self.contador+=1

   def setDecremento(self):
      self.contador-=1
         
   def get_Contador(self):
      return self.contador


