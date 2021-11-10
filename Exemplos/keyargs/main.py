"""
    *keyargs - permite que você passe argumentos de comprimento variável com palavra-chave para uma função.
    Você deve usar **kwargs se quiser lidar com argumentos nomeados em uma função.
"""


def greet_me(**kwargs):
    """
    >>> greet_me(name="yasoob")
    name = yasoob

    :param kwargs:
    :return:
    """
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))
