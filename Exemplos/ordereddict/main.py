"""
    OrderedDict - mantém suas entradas classificadas conforme são inicialmente inseridas.
    Substituir um valor de uma chave existente não altera a posição dessa chave. No entanto, excluir e reinserir
    uma entrada move a chave para o final do dicionário.

    >>> from collections import OrderedDict
    >>> colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
    >>> for key, value in colours.items():
    ...     print(key, value)
    Red 198
    Green 170
    Blue 160
"""