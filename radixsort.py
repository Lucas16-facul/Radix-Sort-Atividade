import random
import time


# Gera 100.000 números inteiros aleatórios
def gerar_lista(tamanho):
    return [random.randint(0, 999999) for _ in range(tamanho)]


# Ordenação auxiliar: Counting Sort por dígito
def counting_sort(lista, expoente):
    tamanho = len(lista)

    resultado = [0] * tamanho
    contagem = [0] * 10

    # Conta a ocorrência de cada dígito
    for numero in lista:
        digito = (numero // expoente) % 10
        contagem[digito] += 1

    # Calcula as posições acumuladas
    for i in range(1, 10):
        contagem[i] += contagem[i - 1]

    # Distribui os números de forma estável
    for i in range(tamanho - 1, -1, -1):
        numero = lista[i]
        digito = (numero // expoente) % 10

        resultado[contagem[digito] - 1] = numero
        contagem[digito] -= 1

    # Atualiza a lista original
    for i in range(tamanho):
        lista[i] = resultado[i]


# Algoritmo Radix Sort
def radix_sort(lista):
    if len(lista) == 0:
        return lista

    maior = max(lista)

    expoente = 1

    # Processa cada casa decimal
    while maior // expoente > 0:
        counting_sort(lista, expoente)
        expoente *= 10

    return lista


# Programa principal
quantidade = 100000

lista = gerar_lista(quantidade)

# Guarda uma cópia para demonstrar a lista original
lista_original = lista.copy()

print("Quantidade de números:", len(lista))
print("Amostra da lista original:", lista_original[:20])

# Mede o tempo de execução
inicio = time.perf_counter()

lista_ordenada = radix_sort(lista)

fim = time.perf_counter()

# Exibe os resultados
print("\nAmostra da lista ordenada:", lista_ordenada[:20])

print("\nTempo de execução:",
      round(fim - inicio, 6), "segundos")

# Verifica se a ordenação está correta
if all(lista_ordenada[i] <= lista_ordenada[i + 1]
       for i in range(len(lista_ordenada) - 1)):
    print("Ordenação realizada com sucesso!")
else:
  print("Erro de Ordenação!")
