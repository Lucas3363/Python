
'''
Escreve o programa Python para uma lista de pessoas identificadas pelo número de telefone, 
cujos dados são nome, endereço, cidade, estado.
Para isto, crie um menu da aplicação com as seguintes atividades:
1-cadastrar 
2-pesquisar
3-alterar
4-excluir
5-listar (pode ser em ordem de nome?)
9-fim
'''

class DictPessoa:
   def __init__(self):
      self.dictPessoa={}

   def cadastrar(self,fone,nome,endereco,cidade,estado):
      dados=[]
      dados.append(nome)
      dados.append(endereco)
      dados.append(cidade)
      dados.append(estado)
      self.dictPessoa.setdefault(fone,dados)

   def getPessoa(self):
      return self.dictPessoa

   def pesquisar(self,fone):
      if self.dictPessoa.get(fone):
         return True
      else:
         return False
   
   def alterar(self,fone,nome,endereco,cidade,estado):
      dados=[]
      dados.append(nome)
      dados.append(endereco)
      dados.append(cidade)
      dados.append(estado)
      self.dictPessoa.update({fone:dados})

   def excluir(self, fone):
      self.dictPessoa.pop(fone)

#APLICAÇÃO   
'''
d=DictPessoa()
d.cadastrar("4444","jose","r. X, 123","Santos","11040130")
d.cadastrar("4455","Pedro","r. Y, 123","Guaruja","11040130")
print(d.getPessoa())
if d.pesquisar("9444"):
   print("Cadastrado")
else:
   print("Não está cadastrado")

d.alterar("4455","Pedro","r. Y, 123","São Vicente","11040130")
print(d.getPessoa())

d.excluir("4455")
print(d.getPessoa())
'''

d=DictPessoa()
opc=1
while opc != 9:
   print("1-cadastrar")
   print("2-pesquisar")
   print("3-alterar")
   print("4-excluir")
   print("5-listar (pode ser em ordem de nome?)")
   print("9-fim")
   opc = int(input("Selecione:"))
   if opc == 1:
      print("Cadastrando")
   elif opc == 2:
      print("Pesquisando")
   elif opc == 3:
      print("Alterando")
   elif opc == 4:
      print("Excluindo")
   elif opc == 5:
      print("Listando")
   elif opc == 9:
      print("Fim....")
   else:
      print("opção inválida")
      
