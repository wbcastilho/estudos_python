"""
    itertools

    intertools.chain - função geradora de combinação
    >>> import itertools
    >>> list(itertools.chain('ABC', range(2)))
    ['A', 'B', 'C', 0, 1]

    >>> list(itertools.chain.from_iterable(enumerate('ABC')))
    [0, 'A', 1, 'B', 2, 'C']

    >>> list(itertools.zip_longest('ABC', range(5)))
    [('A', 0), ('B', 1), ('C', 2), (None, 3), (None, 4)]

    >>> list(itertools.zip_longest('ABC', range(5), fillvalue='?'))
    [('A', 0), ('B', 1), ('C', 2), ('?', 3), ('?', 4)]

    itertools.product
    >>> list(itertools.product('ABC', range(2)))
    [('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]

    >>> list(itertools.product('ABC', repeat=2))
    [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

    itertools.combination
    >>> list(itertools.combinations('ABC', 2))
    [('A', 'B'), ('A', 'C'), ('B', 'C')]

    >>> list(itertools.combinations_with_replacement('ABC', 2))
    [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

    itertools.permutation
    >>> list(itertools.permutations('ABC', 2))
    [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

"""