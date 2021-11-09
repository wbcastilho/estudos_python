def contar_letras(texto: str):
    """
    >>> contar_letras("welber")
    {'w': 1, 'e': 2, 'l': 1, 'b': 1, 'r': 1}
    >>> contar_letras("banana")
    {'b': 1, 'a': 3, 'n': 2}

    :param texto:
    :return:
    """

    # Resolução 1
    """contagem = {}
    for i in texto:
        if i not in contagem:
            contagem[i] = texto.count(i)"""

    # Resolução 2
    contagem = {}
    for i in texto:
        contagem[i] = contagem.get(i, 0) + 1

    return contagem


print(contar_letras("banana"))
