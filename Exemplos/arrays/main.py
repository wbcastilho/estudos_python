"""
    Arrays

    >>> from array import array

    cria um array de números de ponto flutuante com dupla precisão (typecode 'd') a partir de qualquer objeto iterável
    >>> floats = array('d', [1.0, 2.0, 3.14, 1.0])
    >>> print(floats[-1])
    1.0

    append - adiciona um novo item com valor x ao final do vetor
    >>> floats.append(5.0)
    >>> floats
    array('d', [1.0, 2.0, 3.14, 1.0, 5.0])

    count - retorna a quantidade de ocorrências de x no vetor
    >>> floats.count(1.0)
    2

    insert - insere um novo item com o x no vetor antes da posição i. Valores negativos são tratados como sendo em
    relação ao fim do vetor
    >>> floats.insert(0, 10.0)
    >>> floats
    array('d', [10.0, 1.0, 2.0, 3.14, 1.0, 5.0])
"""