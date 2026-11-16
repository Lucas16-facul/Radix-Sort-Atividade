import random
import time

# Algoritmo: Bubble Sort (Ordenação por Troca/Bolha)
# Compara pares vizinhos e troca quando estão fora de ordem.
# A cada passada, o maior elemento "flutua" para o final da lista.

# VANTAGENS:
# 1. Algoritmo mais simples de todos; fácil de ensinar e implementar.
# 2. É "estável" (mantém a ordem relativa de elementos iguais).
# 3. In-place: usa memória extra constante.
# 4. Detecta lista já ordenada em uma única passada (versão otimizada).

# DESVANTAGENS:
# 1. Complexidade O(n²) — o mais lento para listas grandes.
# 2. Faz muitas comparações e trocas, péssimo desempenho na prática.
# 3. Não é usado em aplicações reais, apenas didático.

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        houve_troca = False
        # A cada passada o maior elemento já fica no final,
        # então o laço interno encurta
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                houve_troca = True
        # Se nenhuma troca ocorreu, a lista já está ordenada
        if not houve_troca:
            break
    return lista

if __name__ == "__main__":
    lista = []
    for _ in range(100000):
        lista.append(random.randint(0, 999999))

    inicio = time.perf_counter()
    bubble_sort(lista)
    fim = time.perf_counter()

    print(f"Tempo de execução: {fim - inicio:.2f} segundos")
    print("\nPrimeiros 100 elementos:", lista[:100])
    print("Últimos 100 elementos:", lista[-100:])
