"""
Enunciado do exercicio
https://www.programcreek.com/2015/03/rotate-array-in-java/

Lista:
    >>> lst = [1, 2]
    >>> copia = list(lst)
    >>> copia
    [1, 2]
    >>> copia is lst
    False

String:
    >>> copia_str = str('banana')
    >>> copia_str
    'banana'

Converter String para Lista
    >>> list('banana')
    ['b', 'a', 'n', 'a', 'n', 'a']

Converter Lista para String
    >>> ''.join(['b', 'a', 'n', 'a', 'n', 'a'])
    'banana'
    >>> '-'.join(['b', 'a', 'n', 'a', 'n', 'a'])
    'b-a-n-a-n-a'

Métodos em comum List e String
    >>> s = 'banana'
    >>> lst = ['b', 'a', 'n', 'a', 'n', 'a']
    >>> s[0], lst[0]
    ('b', 'b')
    >>> len(s), len(lst)
    (6, 6)
    >>> s[2:5], lst[2:5]
    ('nan', ['n', 'a', 'n'])
    >>> s[:5], lst[:5]
    ('banan', ['b', 'a', 'n', 'a', 'n'])
    >>> s[4:], lst[4:]
    ('na', ['n', 'a'])
    >>> sorted(s), sorted(lst)
    (['a', 'a', 'a', 'b', 'n', 'n'], ['a', 'a', 'a', 'b', 'n', 'n'])
    >>> lst.sort()
    >>> lst
    ['a', 'a', 'a', 'b', 'n', 'n']
"""
from typing import List


def rotacionar(lista: List, k: int) -> List:
    """
    >>> lista2 = [1, 2, 3, 4, 5, 6, 7]
    >>> list(rotacionar(lista2, 3))
    [5, 6, 7, 1, 2, 3, 4]
    >>> for elemento in rotacionar(lista2, 1):
    ...     print(elemento)
    ...
    4
    5
    6
    7
    1
    2
    3

    :param lista:
    :param k:
    :return:
    """
    for i in range(k):
        resultado = lista.pop(-1)
        lista.insert(0, resultado)
    return lista

