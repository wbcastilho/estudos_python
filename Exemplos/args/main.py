"""
    *args - *args é usado para enviar uma lista de argumentos de comprimento variável sem palavra-chave para a função.
"""


def test_var_args(f_arg, *argv):
    """
    >>> test_var_args('yasoob', 'python', 'eggs', 'test')
    first normal arg: yasoob
    another arg through *argv: python
    another arg through *argv: eggs
    another arg through *argv: test

    :param f_arg:
    :param argv:
    :return:
    """
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)
