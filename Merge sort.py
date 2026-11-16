import random
import time

# O algotirmo merge.sort ele divide a lista ao meio,

#até restarem apenas sublistas,com apenas umn elemento,

#(que já estão ordenados por definição).

#ele também ordena cada lista individualmente,

#e depois ele junta as sublistas duas a duas,comparando

#os elemntosde cada uma e inserindo sempre o menor primeiro,

#Até reconstruir a lista completa já ordenada.


#vantagens;
#O merge sort,sempre faz a mesma coisa
#ele divide a lista em sublistas e junta novamente em ordem.

#se dois elementos têm o mesmo valor de ordenação e um 
# aparece antes do outro na lista de entrada, 
# esse mesmo elemento continuará aparecendo antes na lista 
# ordenada.



#desvantagens;

#o merge sort utiliza muita mémoria RAm da sua máquina

#o merge sort ele não é muito bom para listas pequenas

def merge_sort(lista):
	if len(lista) <= 1:
		return lista

	meio = len(lista) // 2
	esquerda = merge_sort(lista[:meio])
	direita = merge_sort(lista[meio:])
	resultado = []
	i = j = 0

	while i < len(esquerda) and j < len(direita):
		if esquerda[i] <= direita[j]:
			resultado.append(esquerda[i])
			i += 1
		else:
			resultado.append(direita[j])
			j += 1

	resultado.extend(esquerda[i:])
	resultado.extend(direita[j:])
	return resultado


lista = [random.randint(0, 1_000_000) for _ in range(100_000)]
inicio = time.perf_counter()
lista_ordenada = merge_sort(lista)
tempo = time.perf_counter() - inicio
print(f"Tempo de ordenação: {tempo:.6f} segundos")
