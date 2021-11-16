"""
    Expressões Geradoras

    Para inicializar tuplas, arrays e outros tipos de sequencia poderiamos começar também
    com uma listcomp, porem uma genexp economisa memória
    As genexp(Generator Expression) utilizam a mesma sintaxe das listcomps, porém são delimitadas por parênteses

    >>> import array

    Criando uma tupla com genexp
    >>> symbols = 'DEABCFG'
    >>> print(tuple(ord(symbol) for symbol in symbols))
    (68, 69, 65, 66, 67, 70, 71)

    Criando um array como genexp
    >>> array_num = array.array('I', (ord(symbol) for symbol in symbols))
    >>> print(array_num)
    array('I', [68, 69, 65, 66, 67, 70, 71])
"""
