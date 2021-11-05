# Tuplas - Não se pode alterar ou remover intens de uma tupla, ou seja, são valores imutáveis

# Declarando tuplas
sites = ('youtube.com', 'facebook.com', 'instagran.com')
valores = (23, 34, 65)
print(sites[2])
print(valores[0])

# Declarando tuplas
nome_da_tupla = (1, "olá", 1.5)    # tupla heterogênea
print(nome_da_tupla)

# Declarando tuplas
cores_tamanhos = ('vermelho', 'verde', 'azul') + ('alto', 'baixo', 'médio')
print(cores_tamanhos)

# desempacotamento de tuplas
x, y = (9, 10)
print(x)
print(y)

# retornando tuplas em funções
def maior(value):
    ma = value[0]
    pos = 0
    for i in range(1, len(value)):
        if value[i] > ma:
            ma = value[i]
            pos = i
    return ma, pos


x, y = maior([1, 2, 3])
print(x)
print(y)
