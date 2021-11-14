"""
    set - Os sets são uma coleção de itens desordenada, parcialmente imutável e que não podem conter elementos
    duplicados. Por ser parcialmente imutável, os sets possuem permissão de adição e remoção de elementos.
    Além disso, os sets são utilizados, normalmente, com operações matemáticas de união, interseção e diferença
    simétrica, conforme veremos nos próximos tópicos.

    Criar set
    >>> conjunto = {1, 2, 3, 4, 1}
    >>> conjunto
    {1, 2, 3, 4}

    Criar set a partir de um list
    >>> conjunto = set([1, 2, 8, 9])
    >>> conjunto
    {8, 1, 2, 9}

    add - adicionando elementos
    >>> conjunto = {1, 2, 3, 4}
    >>> conjunto.add(5)
    >>> conjunto
    {1, 2, 3, 4, 5}

    update - atualizar conjunto
    >>> conjunto = {1, 2, 3, 4}
    >>> conjunto.update([5, 6, 7])
    >>> conjunto
    {1, 2, 3, 4, 5, 6, 7}

    discard - removendo elementos
    >>> conjunto = {1, 2, 3, 4}
    >>> conjunto.discard(2)
    >>> conjunto
    {1, 3, 4}

    Operações de conjunto
    >>> conjunto_1 = {1, 2, 3, 4, 1}
    >>> conjunto_2 = set([1, 2, 8, 9, 10])

    union - todos os elementos dos dois sets serão “unidos” em um, formando um único set com todos os elementos,
    sem se repetir
    >>> conjunto_1 | conjunto_2
    {1, 2, 3, 4, 8, 9, 10}
    >>> conjunto_1.union(conjunto_2)
    {1, 2, 3, 4, 8, 9, 10}

    intersection - apenas os elementos que estiverem nos dois sets restarão
    >>> conjunto_1 & conjunto_2
    {1, 2}
    >>> conjunto_1.intersection(conjunto_2)
    {1, 2}

    difference - restarão apenas os elementos que estiverem em um dos set, mas não no segundo
    >>> conjunto_1 - conjunto_2
    {3, 4}
    >>> conjunto_1.difference(conjunto_2)
    {3, 4}

    symmetric_difference - apenas os elementos que estiverem nos dois sets, porém que não se repitam, serão exibidos
    >>> conjunto_1 ^ conjunto_2
    {3, 4, 8, 9, 10}
    >>> conjunto_1.symmetric_difference(conjunto_2)
    {3, 4, 8, 9, 10}
"""