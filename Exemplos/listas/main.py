# Listas

# Criar Lista
sites = ['youtube.com', 'facebook.com', 'instagran.com']
print(sites[1])

# Criar Lista
sites = list(['youtube.com', 'facebook.com', 'instagran.com'])
print(sites[1])

# Index
# Utilizado encontrar a posição de um valor especificado
pos = sites.index('youtube.com')
print(f'O item desejado está na posição: {pos}')

# Count
# O método count(elemento) retorna o número de vezes que o valor especificado aparece na lista
pos = sites.count('youtube.com')
print(f'O item desejado aparece: {pos} vez')

# Append
# Para adicionar um elemento ao final da lista, use o método append(elemento)
sites.append('novosite.com')
print(sites)

# Insert
# Para adicionar um item em um índice especificado, use o método insert(índice, elemento)
sites.insert(0, 'google.com')
print(sites)

# Extends
# O método extend(iterável) adiciona os elementos de uma lista especificada (ou qualquer outro iterável) ao final da
# lista
sacola = ['Laranja', 'Banana']
legumes = ['Xuxu', 'Batata']
sacola.extend(legumes)
print(sacola)

# Remove
# Para remover um item com valor especificado, use o método remove(elemento)
sites.remove('facebook.com')
print(sites)

# Del
# Outra forma de remover elementos de uma lista é utilizando a função del do próprio Python
lista = [10, 20, 30, 40, 50]
del lista[2]

# Apagar listas inteiras com Del
lista = [10, 20, 30, 40, 50]
del lista
# print(lista) # gera um erro ao tentar imprimir já que a lista não está mais definida

# Pop
# Para remover um item do índice especificado e ainda retorná-lo, use o método pop(índice)
lista = ['Banana', 'limão', 'Carro', 'Laranja']
item = lista.pop(2)
print('Item:', item)
print('Lista: ', lista)

# Elimina todos os elementos de uma lista
lista = [10, 20, 40, 50]
lista.clear()
print(lista)

# Listas dinâmicas
# Pode-se colocar tipos diferentes em suas listas
sites2 = ['youtube.com', 'facebook.com', 'instagran.com', True, 35]

# Listas de listas
pessoas = [['Rafael', 25], ['Amanda', 19]]
print(pessoas)
print(pessoas[1][0])

# Copy
# Esse método retorna uma cópia da lista especificada
lista = ['Python', 'Academy']
lista_copiada = lista.copy()
print(lista_copiada)

# Reverse
# O método reverse é utilizado para reverter a ordem dos elementos de uma lista
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)

# Sort
lista = [1, 4, 5, 2, 4]
lista.sort()
print(lista)

# Sort -  Ordenar ordem reversa
lista = [1, 4, 5, 2, 4]
lista.sort(reverse=True)
print(lista)