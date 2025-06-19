num1 = int(input("digite um número: "))
num2 = int(input("digite mais um número: "))

soma = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2

print("a soma entre os dois números é: ", soma)
print("a subtração entre os dois números é: ", sub)
print("a divisão entre os dois números é: ", div)
print("a multiplicação entre os dois números é: ", mult)

num1 = int(input("digite um número: "))
num2 = int(input("digite mais um número: "))
opcao = int(input("digite a funcao: 1- soma, 2- sub, 3- multiplicao, 4- div "))


if opcao == 1 :
  soma = num1 + num2
  print(soma)
elif opcao == 2:
  sub = num1 - num2
  print(sub)
elif opcao == 3:
   mult= num1 *num2
   print(mult)
else :
  div == num1 / num2
  print(div)

peso = float(input("me fale seu peso: "))
altura = float(input("me diga a sua altura: "))
print("seu imc é: ", peso / (altura ** 2))

base = float(input("valor da base: "))
alt = float(input("valor da altura: "))
print("A area do triangulo é: ", base * alt / 2)

raio = float(input("digite o valor do raio: "))
print("valor da area da circunferencia: ", raio ** 2 * 3.14)

nota1= float(input("me fale a sua primeira nota: "))
nota2= float(input("me fale a sua segunda nota: "))
resultado= (nota1+nota2)/2
if resultado == 10:
 print("Aprovado com Distinção")
elif resultado >= 7:
 print("Aprovado")
else :
 print('Reprovado')

nu1 = float(input("me fale um numero: "))
nu2 = float(input("me fale outro numero: "))
nu3 = float(input("me fale mais um numero: "))
maior  = nu1
if nu2 > maior:
  maior = nu2
if nu3 > maior:
  maior = nu3
print ("o maior número é: ",maior)

n1 = float(input("me fale um numero: "))
n2 = float(input("me fale outro numero: "))
n3 = float(input("me fale mais um numero: "))

if n1 > n2:
  n1, n2 = n2, n1
if n1 > n3:
  n1, n3 = n3, n1
if n2 > n3:
  n3, n2 = n2, n3
print("A ordem é; " ,n1, "," ,n2, "," ,n3, )

salario = float(input("me informe o seu salario; "))

if salario <= 280:
 percentual = 20
elif salario <= 700:
  percentual = 15
elif salario <= 1500:
  percentual = 10
else:
  percentual = 5

print("seu salario antes do aumento: R$", salario)
print("voce recebue um aumento de: ", percentual, "%")

percentual = percentual /100
aumento = percentual * salario
salario_novo = salario + aumento

print("Você teve um aumento no valor de: R$", aumento)
print("Seu novo salario é no valor de: R$", salario_novo)

litros = float(input("Digite quantos litros você quer abastecer: "))
combustivel = input("Digite A para álcool ou G para gasolina: ")
preco = 0

if combustivel == "A" or combustivel == "a":
    preco = litros * 1.9
    if litros <= 20:
        preco -= 1.9 * litros * 3 / 100
    else:
        preco -= 1.9 * litros * 5 / 100
elif combustivel == "G" or combustivel == "g":
    preco = litros * 2.5
    if litros <= 20:
        preco -= 2.5 * litros * 4 / 100
    else:
        preco -= 2.5 * litros * 6 / 100

print(f"O preço a pagar é R${preco:.2f}")

while True:
  numero = int(input("Digite um númmero: "))

  if numero < 0:
    break
  elif numero % 2 == 0:
    print(" O número é par!")
  elif numero % 2 != 0:
    print(" O número é ímpar!")

while True:
  nota = int(input(" Me fale uma nota: "))

  if  nota >= 0 and nota < 10:
    break
  elif nota < 0 or nota > 10:
    print("Número inválido, tente novamente.")

usuario = input(" Me fale seu usuario: ")

while True:
  senha = input(" Me fale a sua senha:")
  if senha != usuario:
    break
  elif senha == usuario:
    print ("erro!")

while True:
 tab = int(input(" digite um número que você quer a tabuada de multiplicação:  " ))
 n = 0
 if tab == 0:
  break
 else:
   print(f" \n A tabuada de {tab} é: ")
   while n <= 10:
    u = tab * n
    print (tab, 'X', n, '=', u )
    n+=1

fatorial = 1
for numero in range(1,11):
  fatorial = fatorial * numero
  print("fatorial" , numero , "=" , fatorial)

numero = int(input("Me fale um numero: "))

for n in range(1, numero+1):
  if numero % n == 0:
    print(n)

while True:
 tab = int(input(" digite um número que você quer a tabuada de multiplicação ou digite 0 para sair:  " ))
 n = 0
 if tab == 0:
  break
 else:
   print(f" \n A tabuada de {tab} é: ")
   for n in range(1,10):
    u = tab * n
    print (tab, 'X', n, '=', u )
    n+=1

for i in range(0,30):
  if i > 1:
    for n in range(2,i):
      if(i % n == 0):
         break
    else:
      print(i)

n = int(input("Digite o tamanho da lista: "))
lista = []

for i in range(n):
  lista.append(int(input()))

x = int(input("Digite o número que será procurado: "))

if x in lista:
  print("O valor da lista!")
else:
    print("O valor não está na lista!")

lista = []

while True:

  numero = (int(input()))
  if numero > 0:
    lista.append(numero)
  else:
    break


x = int(input("Digite o número que será procurado: "))

if x in lista:
  print("O valor da lista!")
else:
    print("O valor não está na lista!")

vingadores = ["Homem de Ferro", "Capitão América", "Thor", "Hulk", "Viúva Negra", "Gavião Arqueiro"]

vingadores.append("Homem Aranha")

print(f"Thor está na posição: ",vingadores.index("Thor"))

vingadores.remove("Homem de Ferro")
vingadores.remove("Viúva Negra")

print(vingadores)

n = int(input("Digite a qunatidade de elementos: "))
lista = []

for i in range(n):
  elemento = int(input("Digite o numero: "))
  lista.append(elemento)

for i in lista:
  if i % 2 == 0:
     lista.remove(i)

print(lista)

n = int(input("Digite o tamanho da turma: "))
t1 = []
t2 = []

for i in range(n):
  notas =  float(input("Digite as notas t1: "))
  t1.append(notas)
for i in range(n):
  notas =  float(input("Digite as notas t2: "))
  t2.append(notas)

print (t1, t2)

print(f'A média da turma 1 é:  {sum (t1)//n} A média da turma 2 é:  {sum (t2)//n}')

if sum(t1)//n == sum(t2)//n:
  print("As duas turmas estão empatadas, parabéns!")
elif sum(t1)//n > sum(t2)//n:
  print("A turma que obteve a melhor nota da prova foi a turma 1")
else:
  print("A turma que obteve a melhor nota da prova foi a turma 2")

n = int(input("Digite o tamanho da sua lista: "))
l1 = []
l2 = []

for i in range(n):
  lista =  float(input("Digite os elementos da lista 1: "))
  l1.append(lista)
for i in range(n):
  lista =  float(input("Digite os elementos da lista 2: "))
  l2.append(lista)

l3 = l1 + l2
print ("A ordem em que foi digitada: ", l3)

l3.sort()
print("L3 na ordem crescente: ", l3)

l3.reverse()
print("L3 na ordem decrescente: ", l3)

dados = [
 {"dia": 12, "mes": 2, "ano": 2019, "temp": 30.5},
 {"dia": 18, "mes": 3, "ano": 2019, "temp": 29.1},
 {"dia": 22, "mes": 4, "ano": 2019, "temp": 28.5},
 {"dia": 17, "mes": 5, "ano": 2019, "temp": 26.4}
 ]

for item in dados:
  print(f'{item["dia"]}/{item["mes"]}/{item["ano"]}:temp:{item["temp"]}')

n = int(input("Quantos Pokémon você quer adicionar? "))
pokemon = {}

for i in range(n):
 nome = input()
 tipo = input().lower()
 ataque = int(input())
 pokemon[nome] = {"tipo": tipo, "ataque": ataque}
#print(pokemon)
#print(pokemon["joao"]["tipo"])

maior_ataque = 0
nome_maior_ataque = ''

for nome, tipo_ataque in pokemon.items():
  if tipo_ataque[0] == "fogo":
    if tipo_ataque[1] > maior_ataque:
      maior_ataque = tipo_ataque[1]
      nome_maior_ataque = nome

print(f"Pokemon de fogo com maior ataque é: {nome_maior_ataque}")

entrada = input("Digite uma frase: ")
frase_in = ""
tamanho = len(entrada) - 1
for i in range((tamanho),-1,-1):
  print(i)
  frase_in = frase_in + entrada[i]

print(frase_in)

entrada = input('Digite uma frase: ')
print(entrada [::-1])

entrada = input('Digite uma frase: ')
entrada1 = entrada[::-1]

if entrada == entrada1:
  print(f"A palavra {entrada} é um palidromo.")
else:
   print(f"a palavra {entrada} não é um palidromo.")

entrada = input('Digite uma frase: ')
entrada1 = entrada.lower()

if entrada == entrada1:
  print(f"Todas a letras \"{entrada}\" são minusculas.")
else:
   print(f"Nem todas as letras {entrada} são minusculas.")

entrada = input('Digite uma frase: ')
entrada1 = entrada.upper()

if entrada == entrada1:
  print(f"Todas a letras \"{entrada}\" são maiuscula.")
else:
   print(f"Nem todas as letras {entrada} são maiuscula.")

entrada = input("Digite uma frase: ")
entrada1 = ""

for i in range(len(entrada)):
  if entrada[i].isupper():
    entrada1 += entrada[i].lower()
  else:
    entrada1 += entrada[i].upper()

print(f"A frase \"{entrada}\" com as letras maiusculas e minusculas trocada é: \"{entrada1}\"")

cod = []
alt = []
pes = []
x = 0
med = 0
while True:
  info = int(input("Digite o código ou 0 para finalizar: "))
  if info == 0:
    break
  else:
    cod.append(info)
    info = float(input("Digite a altura: "))
    alt.append(info)
    info = float(input("Digite a peso: "))
    pes.append(info)

x = alt.index(max(alt))
print(f"\nCliente mais alto:\nCodigo:{cod[x]} Altura:{alt[x]} Peso:{pes[x]}")
x = alt.index(min(alt))
print(f"\nCliente mais baixo:\nCodigo:{cod[x]} Altura:{alt[x]} Peso:{pes[x]}")
x = pes.index(max(pes))
print(f"\nCliente mais gordo:\nCodigo:{cod[x]} Altura:{alt[x]} Peso:{pes[x]}")
x = pes.index(min(pes))
print(f"\n2Cliente mais magro:\nCodigo:{cod[x]} Altura:{alt[x]} Peso:{pes[x]}")
i = 0
for i in range(0, len(alt)):
  med=0
  med = alt[i] + med
  i+=1
print(f"A media da altura é: {med}")
i = 0
for i in range(0, len(pes)):
  med=0
  med = pes[i] + med
  i+=1
print(f"A media do peso é: {med}")

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)

print("Qual o melhor Sistema operacional para uso em servidores? ")
print('1- Windows Serve', '2- Unix', ' 3- Linux', '4- Netware', '5- Mac Os', '6- Outros')
votos = []

while True:
  opcao = int(input("Digite a opção desejada: "))
  if opcao == 0:
    break
  elif opcao > 6 or opcao < 0:
    print("Opção inválida.")
  else:
    votos.append(opcao)


# votos.cont(1)
# print(len(votos))

print(f''' Sistema Operacional    Votos    %
-------------------      -----   -----
Whindows Serve           {votos.count(1)}            {votos.count(1) * 100 / len (votos)}
Unix                     {votos.count(2)}            {votos.count(2) * 100 / len (votos)}
Linux                    {votos.count(3)}            {votos.count(3) * 100 / len (votos)}
Netware                  {votos.count(4)}            {votos.count(4) * 100 / len (votos)}
Mac OS                   {votos.count(5)}            {votos.count(5) * 100 / len (votos)}
Outro                    {votos.count(6)}            {votos.count(6) * 100 / len (votos)}
-------------------      -----
Total                      {len(votos)}
''')


print("Digite os nomes que você deseja inserir na lista ou didgite 0 para sair: ")
lista = []

while True:
  n = input()
  if n == "0" :
    break
  lista.append(n)

nome=  input("Qual nome eu devo procurar? ")
for i in lista:
  if nome == i:
   print(nome, "Pertence a lista")
   print(lista.index(nome))
   break


# if nome in lista:
#   print(nome, "Pertence a lista")
#   print(len(nome))
# else:
#  print(nome,"Não pertence a lista")

cor = input("Me fale a cor do cd's que você deseja saber o valor. ")

if cor == "verde":
  print("O valor do cd na cor verde é R$10,00")
elif cor == "azul" :
   print("O valor do cd na cor azul é R$20,00")
elif cor == "amarelo":
  print("O valor do cd na cor amarelo é R$30,00")
elif cor == "vermelho":
  print("O valor do cd na cor vermelho é R$40,00")

carros = ['fusca', 'gol', 'vectra', 'golf', 'civic']
consumo = [5, 25, 36, 41, 20]
menor_consumo = min(consumo)
menor_consumo_index = consumo.index(menor_consumo)
print (f'O carro mais econômico é: {carros[menor_consumo_index]}')
print(f"O fusca irá gastar para percorre 1000km; R${(1000/5)*4.25}")
print(f"O gol irá gastar para percorre 1000km; R${(1000/25)*4.25}")
print(f"O vectra irá gastar para percorre 1000km; R${(1000/36)*4.25:.2f}")
print(f"O golf irá gastar para percorre 1000km; R${(1000/41)*4.25:.2f}")
print(f"O civic irá gastar para percorre 1000km; R${(1000/20)*4.25}")

print("Digite qual o melhor sistema operacional para uso em servidores? ")
print('1- Windows Server, 2- Unix, 3- Linux, 4- Netware, 5- Mac Os, 6-Outros')
votos = []

while True:
  n = int(input())
  if n == 0:
    break
  elif n < 0 or n > 6:
    print('opção invalida')
  else:
   votos.append(n)


print(f'''

Windwos Serve           {votos.count(1)}            {votos.count(1) * 100 / len (votos)}
Unix                    {votos.count(2)}            {votos.count(2) * 100 / len (votos)}
Linux                   {votos.count(3)}            {votos.count(3) * 100 / len (votos)}
Netware                 {votos.count(4)}            {votos.count(4) * 100 / len (votos)}
Mac                     {votos.count(5)}            {votos.count(5) * 100 / len (votos)}
Outros                  {votos.count(6)}            {votos.count(6) * 100 / len (votos)}

Total                   {len(votos)}
     ''' )

destino = input("Me informe o destino da sua Viajem. ")
km = float(input("Me informe a distância até o seu destino em quilômetros. "))
consumo_medio = float(input("Me e informe o consumo medio de combustível do seu veículo em quilômetros por litros. "))
preço = float(input("Me informe o valor do combustível por litros. "))

while True:
  n = float(input(" Me informe os valores dos custos adicionais: e quando terminar digite 0 para sair. "))
  if n == 0:
    break
  else:
   custos_adicionais = [n]

combustivel = (consumo_medio / preço) * km

print (f'o seu custo total para essa viagem é de: ', {n + combustivel})

def e_par(num):
 if num % 2 == 0:
   return 'é par'
 else:
   return "é impar"

def main():
 while True:
  num = int(input("digite um numero"))
  if num == -1:
   break
  else:
   print(e_par(num))

main()
# if num % 2 == 0:
#   print ('é par')
# else:
#   print ("é impar")

class Pessoa:
  def __init__(self, nome, idade, profissao):
   self.nome = nome
   self.idade = idade
   self.profissao = profissao

  def falar(self, frase):
    print(frase)

pessoa1 = Pessoa("Ingrid", 19, "estudante")
pessoa1.falar("Olá!")
pessoa1.nome = "Yana"
print(pessoa1.nome, pessoa1.idade)

class Conta:
  def __init__(self, nome, cpf, numero, saldo = 0):
    self.nome = nome
    self.cpf = cpf
    self.numero = numero
    self.saldo = saldo

  def vernome(self):
    print("O nome é: ", self.nome)

  def vernumero(self):
    print("O numero é: ", self.numero)

  def versaldo(self):
    print("O seu saldo é: ", self.saldo)

  def deposito(self, valor):
   self.saldo +=valor
   print("O seu novo saldo é: ", self.saldo)
  def saque(self, valor):
    self.saldo -=valor
    print("O seu saldo atual é: ", self.saldo)

conta = Conta("Ingrid", "123", "000")
conta.vernome()
conta.vernumero()
conta.versaldo()
conta.deposito(100)
conta.saque(50)

def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("me fale um número: "))
num2 = int(input("me fale mais um número: "))
resultado = mdc(num1,num2)
print(f'o mdc dos número informados é {resultado}')

def mmc(a, b):
    return a * b // mdc(a, b)

num1 = int(input("me fale um número: "))
num2 = int(input("me fale mais um número: "))
resultado = mmc(num1,num2)
print(f'o mmc dos número informados é {resultado}')

import math

def mdc_lista(lista_numeros):
    resultado = lista_numeros[0]
    for numero in lista_numeros[1:]:
      resultado = math.gcd(resultado, numero)
    return resultado


numeros = [48, 18, 12]
resultado = mdc_lista(numeros)
print(f'O mdc da lista {numeros} é {resultado}')

def mmc_lista(lista_numeros):

    resultado = lista_numeros[0]
    for numero in lista_numeros[1:]:
        resultado = (resultado * numero) // mdc(resultado, numero)
    return resultado

numeros = [48, 18, 12]
resultado = mmc_lista(numeros)
print(f'O mmc da lista {numeros} é {resultado}')

def elementos_unicos(lista):
    return list(set(lista))

lista_original = [1, 2, 2, 3, 4, 4, 5]
lista_sem_repeticoes = elementos_unicos(lista_original)
print(lista_sem_repeticoes)

def moda_lista(lista):
  contagem = (lista)
  frequencia_maxima = max(contagem.values())
  moda = [elemento for elemento, frequencia in contagem.items() if frequencia == frequencia_maxima]
  return moda

lista_original = [1, 2, 2, 3, 3, 4, 4, 5, 5, 5]
moda = moda_lista(lista_original)
print("A moda da lista é:", moda)

def uniao_de_conjuntos(conjunto1, conjunto2):
    conjunto_uniao = set(conjunto1).union(conjunto2)
    return list(conjunto_uniao)

conjunto1 = [1, 2, 3, 4, 5]
conjunto2 = [4, 5, 6, 7, 8]
resultado = uniao_de_conjuntos(conjunto1, conjunto2)
print("União dos conjuntos:", resultado)

def subconjunto(conjunto1, conjunto2):
    return set(conjunto1).issubset(conjunto2)

conjunto1 = [1, 2, 3]
conjunto2 = [1, 2, 3, 4, 5]
resultado = subconjunto(conjunto1, conjunto2)
if resultado:
    print("conjunto1 é um subconjunto de conjunto2.")
else:
    print("conjunto1 não é um subconjunto de conjunto2.")

def diferenca_de_conjuntos(conjunto1, conjunto2):
    diferenca = list(set(conjunto1).difference(conjunto2))
    return diferenca

conjunto1 = [1, 2, 3, 4, 5]
conjunto2 = [4, 5, 6, 7, 8]
resultado = diferenca_de_conjuntos(conjunto1, conjunto2)
print("Diferença entre os conjuntos:", resultado)