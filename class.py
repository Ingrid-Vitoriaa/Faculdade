class UsuarioJogo():
  def __init__(self, nome, nickname):
    self.__nome = nome
    self.__nickname = nickname
    self.__pontuacao = 0
    self.__nivel = 1

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome):
    self.__nome = nome

  @property
  def nickname(self):
    return self.__nickname

  @nickname.setter
  def nickname(self, nickname):
    self.__nickname = nickname

  @property
  def pontuacao(self):
    return self.__pontuacao

  @pontuacao.setter
  def pontuacao(self, pontuacao):
    self.__pontuacao = pontuacao

  @property
  def nivel(self):
    return self.__nivel

  @nivel.setter
  def nivel(self, nivel):
    self.__nivel = nivel

  def AumentarPontuacao(self):
    self.__pontuacao += 1

  def SubirNivel(self):
    self.__nivel += 1

  def Bonus(self, bonus):
    self.pontuacao += bonus

n1 = UsuarioJogo("Paulo", "Gamerbr123")
n1.SubirNivel()
n1.AumentarPontuacao()
n1.Bonus(30)

n2 = UsuarioJogo("claudio", "NoobMaster69")
n2.SubirNivel()
n2.SubirNivel()
n2.AumentarPontuacao()
n2.Bonus(20)

print(f"Usuario 1: Nome: {n1.nome}, Nickname: {n1.nickname}, Pontuação: {n1.pontuacao}, Nível: {n1.nivel}")
print(f"Usuario 2: Nome: {n2.nome}, Nickname: {n2.nickname}, Pontuação: {n2.pontuacao}, Nível: {n2.nivel}")