"""
    Counter - Contador nos permite contar as ocorrências de um determinado item.

    >>> from collections import Counter

    >>> colours = (
    ...    ('Yasoob', 'Yellow'),
    ...    ('Ali', 'Blue'),
    ...    ('Arham', 'Green'),
    ...    ('Ali', 'Black'),
    ...    ('Yasoob', 'Red'),
    ...    ('Ahmed', 'Silver'),
    ... )

    >>> favs = Counter(name for name, colour in colours)
    >>> print(favs)
    Counter({'Yasoob': 2, 'Ali': 2, 'Arham': 1, 'Ahmed': 1})
"""