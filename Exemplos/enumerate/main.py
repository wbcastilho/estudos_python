"""
    enumerate

    >>> my_list = ['apple', 'banana', 'grapes', 'pear']
    >>> for counter, value in enumerate(my_list):
    ...     print(counter, value)
    0 apple
    1 banana
    2 grapes
    3 pear

    Enumera as letras da palavra, começando em 1
    >>> list(enumerate('albatroz', 1))
    [(1, 'a'), (2, 'l'), (3, 'b'), (4, 'a'), (5, 't'), (6, 'r'), (7, 'o'), (8, 'z')]

"""