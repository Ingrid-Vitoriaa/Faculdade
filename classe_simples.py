class Pessoa:

 def __init__(self, nome, cpf):
  self.__nome = nome
  self.__cpf = cpf

 @property
 def nome (self):
  return self.__nome

 @nome.setter
 def nome (self, nome):
  self.__nome = nome

 @property
 def cpf(self):
  return self.__cpf

 @cpf.setter
 def cpf (self, cpf):
  self.__cpf = cpf

p1 = Pessoa("Ingrid", "123")
print(p1.nome)
print (p1.cpf)

p1 = Pessoa("Ingrid", "123")
print(p1.nome)
print (p1.cpf)