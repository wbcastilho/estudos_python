# Não silenciar exceções

# Maneira errada
try:
    do_something()
except:
    pass

# Maneira correta
# Silenciar somente a exceção desejada de maneira explicita
try:
    do_something()
except CustomError:
    pass

# Outra Maneira Correta
# Utilizando gerenciador de contexto a partir do python 3 com a biblioteca contextlib
# Funciona como no caso anterior
with contextlib.suppress(CustomError):
    do_something()