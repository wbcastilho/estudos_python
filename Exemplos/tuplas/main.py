"""
    Tuplas - Não se pode alterar ou remover intens de uma tupla, ou seja, são valores imutáveis

    Declarando tuplas
    >>> sites = ('youtube.com', 'facebook.com', 'instagran.com')
    >>> sites
    ('youtube.com', 'facebook.com', 'instagran.com')

    Declarando tuplas
    >>> valores = (23, 34, 65)
    >>> valores
    (23, 34, 65)

    Declarando tuplas heterogêneas
    >>> nome_da_tupla = (1, "olá", 1.5)
    >>> nome_da_tupla
    (1, 'olá', 1.5)

    Desempacotamento de tuplas
    >>> x, y = (9, 10)
    >>> x, y
    (9, 10)

    Desempacotamento de tuplas
    >>> lax_cordinates = (33.9425, -118.48056)
    >>> latitude, longitude = lax_cordinates
    >>> latitude
    33.9425
    >>> longitude
    -118.48056

    Usando * para capturar itens excedentes
    >>> a, b, *rest = range(5)
    >>> a, b, rest
    (0, 1, [2, 3, 4])

    Usando * para capturar itens excedentes
    >>> a, *body, c, d = range(5)
    >>> a, body, c, d
    (0, [1, 2], 3, 4)

    Usando * para capturar itens excedentes
    >>> *a, b, c, d = range(5)
    >>> a, b, c, d
    ([0, 1], 2, 3, 4)

    Tuplas nomeadas
    >>> from collections import namedtuple
    >>> City = namedtuple('City', 'name country population coordinates')
    >>> tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    >>> tokyo
    City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
    >>> tokyo.population
    36.933
    >>> tokyo.coordinates
    (35.689722, 139.691667)
    >>> tokyo[1]
    'JP'

"""


# retornando tuplas em funções
def maior(value):
    """
    >>> x, y = maior([1, 2, 3])
    >>> x
    3
    >>> y
    2

    :param value:
    :return:
    """
    ma = value[0]
    pos = 0
    for i in range(1, len(value)):
        if value[i] > ma:
            ma = value[i]
            pos = i
    return ma, pos
