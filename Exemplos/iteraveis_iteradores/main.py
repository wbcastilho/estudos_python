"""
    iterável
    Qualquer objeto a partir do qual a função embutida iter pode obter um iterador.
    Objetos que implementem um método __iter__ que devolva um iterador são iteráveis.
    Sequências sempre são iteráveis, assim como objetos que implementem um método __getitem__ que aceite índices a
    partir de 0.

    iterador
    Qualquer objeto que implemente o método __next__, sem argumentos, que devolva o próximo item de uma série ou levante
    StopIteration quando não houver mais itens.
    Os iteradores em Python também implementam o método __iter__, portanto também são iteráveis.

    Verifica se a lista possui o método next, como não possui significa que lista não é um iterador,
    é apenas um iterável
    >>> lista = [0, 1, 2, 3, 4]
    >>> print(hasattr(lista, '__next__'))
    False

    A função inter transforma uma lista em um iterador
    >>> lista = [0, 1, 2, 3, 4, 5]
    >>> lista_iter = iter(lista)
    >>> print(hasattr(lista_iter, '__next__'))
    True

    Como lista_iter é iterável é então possível chamar o método next
    >>> print(next(lista_iter))
    0
    >>> print(next(lista_iter))
    1
    >>> print(next(lista_iter))
    2
    >>> print(next(lista_iter))
    3
    >>> print(next(lista_iter))
    4
    >>> print(next(lista_iter))
    5

    yield
    >>> def gera():
    ...     for n in range(100):
    ...         yield n
    >>> g = gera()
    >>> print(type(g))
    <class 'generator'>

    Expressão geradora
    >>> lista_gerador = (x for x in range(100))
    >>> print(type(lista_gerador))
    <class 'generator'>
"""