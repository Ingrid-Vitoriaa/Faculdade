import time

def tempo(funcao):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        tempo_total = fim - inicio
        print(f"A função {funcao.__name__} levou {tempo_total:.8f} segundos para ser executada.")
        return resultado
    return wrapper

melhor_caso = [("Pizza", 30), ("Espagueti à bolonhesa", 35), ("Feijoada", 40)]
medio_caso = [("Pizza", 30), ("Feijoada", 40), ("Espagueti à bolonhesa", 35)]
pior_caso = [("Feijoada", 40), ("Espagueti à bolonhesa", 35), ("Pizza", 30)]

@tempo
def main(cenario):
    for i in range(1, len(cenario)):
        j = i
        while j > 0 and cenario[j-1][1] > cenario[j][1]:
            cenario[j], cenario[j-1] = cenario[j-1], cenario[j]
            j -= 1
    return cenario

    print("Melhor caso:")
    main(melhor_caso)

    print("Caso médio:")
    main(medio_caso)

    print("Pior caso:")
    main(pior_caso)

@tempo
def busca_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == item:
            return meio
        elif lista[meio] > item:
            fim = meio - 1
        else:
            inicio = meio + 1
    return None

produtos = ["Maçã", "Banana", "Laranja", "Pera", "Uva"]

print("Melhor caso:")
busca_binaria(produtos, "Laranja")

print("Caso médio:")
busca_binaria(produtos, "Banana")

print("Pior caso:")
busca_binaria(produtos, "Uva")