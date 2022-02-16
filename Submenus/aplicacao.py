# Aplicação - Controle Remoto Ar-condicionado (Interface do Usuário) #
# PROJETO CONTROLE DE AR CONDICIONADO - ANDRÉ MOUTINHO #

import classe

ctrl = classe.ArCondicionado()

MenuControle = (
'''=======================================
    CONTROLE REMOTO AR-CONDICIONADO
=======================================
[1] - Ligar
[2] - Aumentar Temperatura
[3] - Diminuir Temperatura
[0] - Desligar
======================================='''
)

cmd  = 0
while cmd != 4:
      Temp = ctrl.buscarValorTemperatura()
      print(f"Temperatura Atual: {Temp}")
      Estado = ctrl.buscarEstadoLigadoDesligado()
      print(f"Estado atual: {Estado}")
      print("\n")
      print(MenuControle)            
      cmd = input("Selecione uma Opção:")      
      if cmd == '1':            
         print("Ligando Ar-condicionado...")
         ctrl.ligar()
         print("\n")
      elif cmd == '+':
         print("Aumentar Temperatura...")
         ctrl.aumentar()
      elif cmd == '-' and ctrl.buscarValorTemperatura()>0:
         print("Diminuir Temperatura...")
         ctrl.diminuir()
      elif cmd == '0':
         print("Desligando Ar-condicionado...")         
         ctrl.desligar()
      else:
         print("OPÇÃO INVÁLIDA: Selecione uma opção válida !") 