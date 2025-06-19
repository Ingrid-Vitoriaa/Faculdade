def bubble_sort(arr):
    tamanho = len(arr)
    for i in range(tamanho):
        for j in range(0, tamanho-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
array_ordenada = bubble_sort(arr)
print (f"Array ordenada: {array_ordenada}" )

def contador_bubble_sort(arr):
    tamanho = len(arr)
    comparacao = 0
    trocas = 0
    for i in range(tamanho):
        for j in range(0, tamanho-i-1):
            comparacao += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocas += 1
    return arr, comparacao, trocas

arr = [64, 34, 25, 12, 22, 11, 90]
array_ordenada, comparacao, trocas = contador_bubble_sort(arr)

print(f"Array ordenada: {array_ordenada}")
print(f"comparacoes: {comparacao}")
print(f"trocas: {trocas}")

def bubble_sort_otimizado(arr):
    tamanho = len(arr)
    comparacao = 0
    trocas = 0
    for i in range(tamanho):
        trocado = False
        comparacao += 1
        for j in range(0, tamanho-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocas += 1
                trocado = True
        if not trocado:
            break
    return arr, comparacao, trocas

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array_ordenada, comparacao, trocas = bubble_sort_otimizado(arr)

print(f"Array ordenada: {array_ordenada}")
print(f"comparacoes: {comparacao}")
print(f"trocas: {trocas}")

def bubble_sort_strings(arr):
    tamanho = len(arr)
    for i in range(tamanho):
        for j in range(0, tamanho-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = ["banana", "apple", "cherry", "date"]
array_ordenada = bubble_sort_strings(arr)
print(f"array ordenada: {array_ordenada}")

def bubble_sort_strings(arr):
    tamanho = len(arr)
    for i in range(tamanho):
        for j in range(0, tamanho-i-1):
            if arr[j].lower() > arr[j+1].lower():
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = ["banana", "Apple", "cherry", "date"]
array_ordenada = bubble_sort_strings(arr)
print(f"array ordenada ignorando maiúsculas e minúsculas: {array_ordenada}")

def bubble_sort_strings_original(arr):
    tamanho = len(arr)
    comparacoes = 0
    for i in range(tamanho):
        for j in range(0, tamanho-i-1):
            comparacoes += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, comparacoes

arr = ["banana", "Apple", "cherry", "date"]
array_ordenada, comparacoes = bubble_sort_strings_original(arr)
print(f"arr ordenada: {array_ordenada}")
print(f"Total de comparações (original): {comparacoes}")

def bubble_sort_strings_otimizado(arr):
    tamanho = len(arr)
    comparacoes = 0
    for i in range(tamanho):
        for j in range(0, tamanho-i-1):
            comparacoes += 1
            if arr[j].lower() > arr[j+1].lower():
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, comparacoes

arr = ["banana", "Apple", "cherry", "date"]
array_ordenada, comparacoes = bubble_sort_strings_otimizado(arr)
print(f"array ordenada ignorando maiúsculas e minúsculas: {array_ordenada}")
print(f"Total de comparações: {comparacoes}")
