# Dicionários
pessoa = {
    'Nome': 'Matheus',
    'Idade': 19,
    'Altura': 168
}
print(pessoa)

# Criar dicionário por meio de função
filme = dict(nome="Home-Aranha", ano="2025", nota="8")
print(filme)

# Selecionando valores em um dicionário
x = {1:10, 2:20, 3:30}
print(x)
print(x[1])
print(x.get(1))

# Caso utiliza duas chaves iguais só retorna a ultima
y = {1:6, 1:9}
print(y)