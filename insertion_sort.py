import random
import time


# insertion sort:
# vantagens: simples de fazer, não gasta memória extra (in-place) e voa se a lista já tiver quase ordenada
# desvantagens: sofre demais com lista gigante por ser o(n^2) no pior caso
def insertion_sort(lista):
  # passa por todo mundo a partir do segundo item
  for i in range(1, len(lista)):
    chave = lista[i]  # o item da vez que a gente quer encaixar
    j = i - 1

    # empurra os maiores pra frente abrindo espaço
    while j >= 0 and lista[j] > chave:
      lista[j + 1] = lista[j]
      j -= 1

    # joga a chave no buraco que sobrou
    lista[j + 1] = chave
  return lista


# cria a lista com 100k itens aleatórios (aqui vai demorar um bocado pra rodar por causa da desvantagem ali de cima)
tamanho = 100000
lista = [random.randint(1, 1000000) for _ in range(tamanho)]

# roda e marca o tempo
inicio = time.perf_counter()
insertion_sort(lista)
fim = time.perf_counter()

# joga na tela o tempo e as pontas da lista
print(f"tempo: {fim - inicio:.4f}s\n")
print(f"primeiros 100:\n{lista[:100]}\n")
print(f"últimos 100:\n{lista[-100:]}")