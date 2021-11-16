"""
    Listas

    Criar Listas
    >>> sites = ['youtube.com', 'facebook.com', 'instagran.com']
    >>> sites[1]
    'facebook.com'

    Criar Lista
    >>> sites = list(['youtube.com', 'facebook.com', 'instagran.com'])
    >>> sites[1]
    'facebook.com'

    Listas dinâmicas - Pode-se colocar tipos diferentes em suas listas
    >>> lista_dinamica = ['youtube.com', 'facebook.com', 'instagran.com', True, 35]
    >>> lista_dinamica
    ['youtube.com', 'facebook.com', 'instagran.com', True, 35]

    Listas de listas
    >>> pessoas = [['Rafael', 25], ['Amanda', 19]]
    >>> print(pessoas)
    [['Rafael', 25], ['Amanda', 19]]
    >>> print(pessoas[1][0])
    Amanda

    len - Retorna a quantidade de intens da lista
    >>> len(sites)
    3

    index - Utilizado encontrar a posição de um valor especificado
    >>> pos = sites.index('youtube.com')
    >>> print(f'O item desejado está na posição: {pos}')
    O item desejado está na posição: 0

    count - O método count(elemento) retorna o número de vezes que o valor especificado aparece na lista
    >>> pos = sites.count('youtube.com')
    >>> print(f'O item desejado aparece: {pos} vez')
    O item desejado aparece: 1 vez

    append - Para adicionar um elemento ao final da lista, use o método append(elemento)
    >>> sites.append('novosite.com')
    >>> print(sites)
    ['youtube.com', 'facebook.com', 'instagran.com', 'novosite.com']

    insert - Para adicionar um item em um índice especificado, use o método insert(índice, elemento)
    >>> sites.insert(0, 'google.com')
    >>> print(sites)
    ['google.com', 'youtube.com', 'facebook.com', 'instagran.com', 'novosite.com']

    extend - O método extend(iterável) adiciona os elementos de uma lista especificada (ou qualquer outro iterável)
    ao final da
    >>> sacola = ['Laranja', 'Banana']
    >>> legumes = ['Xuxu', 'Batata']
    >>> sacola.extend(legumes)
    >>> print(sacola)
    ['Laranja', 'Banana', 'Xuxu', 'Batata']

    remove - Para remover um item com valor especificado, use o método remove(elemento)
    >>> sites.remove('facebook.com')
    >>> print(sites)
    ['google.com', 'youtube.com', 'instagran.com', 'novosite.com']

    pop - Para remover um item do índice especificado e ainda retorná-lo, use o método pop(índice)
    >>> lista = ['Banana', 'limão', 'Carro', 'Laranja']
    >>> item = lista.pop(2)
    >>> print('Item:', item)
    Item: Carro
    >>> print('Lista: ', lista)
    Lista:  ['Banana', 'limão', 'Laranja']

    clear - Elimina todos os elementos de uma lista
    >>> lista = [10, 20, 40, 50]
    >>> lista.clear()

    del - Outra forma de remover elementos de uma lista é utilizando a função del do próprio Python
    >>> lista = [10, 20, 30, 40, 50]
    >>> del lista[2]
    >>> lista
    [10, 20, 40, 50]

    apagar listas inteiras com Del
    >>> lista = [10, 20, 30, 40, 50]
    >>> del lista

    copy - Esse método retorna uma cópia rasa da lista especificada
    >>> lista = ['Python', 'Academy']
    >>> lista_copiada = lista.copy()
    >>> lista_copiada
    ['Python', 'Academy']

    reverse - O método reverse é utilizado para reverter a ordem dos elementos de uma lista
    >>> lista = [1, 2, 3, 4, 5]
    >>> lista.reverse()
    >>> lista
    [5, 4, 3, 2, 1]

    sort
    >>> lista = [1, 4, 5, 2, 4]
    >>> lista.sort()
    >>> lista
    [1, 2, 4, 4, 5]

    sort -  Ordenar ordem reversa
    >>> lista = [1, 4, 5, 2, 4]
    >>> lista.sort(reverse=True)
    >>> lista
    [5, 4, 4, 2, 1]

    sorted - Ordena gerando uma nova lista e mantem a lista passada intacta
    >>> lista = [1, 4, 5, 2, 4]
    >>> lst = sorted(lista)
    >>> lista, lst
    ([1, 4, 5, 2, 4], [1, 2, 4, 4, 5])

    list comprehensions ou listcomp
    >>> symbols = 'GHYIJOLK'
    >>> codes = [ord(symbol) for symbol in symbols]
    >>> print(codes)
    [71, 72, 89, 73, 74, 79, 76, 75]
    >>> numeros = range(0, 35)
    >>> print([numero for numero in numeros if numero % 2 == 0])
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]
"""