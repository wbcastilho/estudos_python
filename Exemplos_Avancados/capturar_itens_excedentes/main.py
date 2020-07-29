# Usando * para capturar itens excedentes
# Definir parâmetros de função com *args para capturar quaisquer argumentos
# em excesso é um recusro clássico em python

# Exemplo 1
a, b, *rest = range(5)
print(a, b, rest)

# Exemplo 2
a, b, *rest = range(3)
print(a, b, rest)

# Exemplo 3
a, b, *rest = range(2)
print(a, b, rest)

# Exemplo 4
a, *body, c, d = range(5)
print(a, body, c, d)

# Exemplo 5
*head, b, c, d = range(5)
print(head, b, c, d)