# Dicionários

# Criar dicionário
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
x = {1: 10, 2: 20, 3: 30}
print(x[1])
print(x.get(1))

# Caso utiliza duas chaves iguais só retorna a ultima
y = {1: 6, 1: 9}
print(y)

# Verificar se a chave passada existe no dicionário
contatos = {'Yan': '1234-5678', 'John': '3267-1855'}
print('Yan' in contatos)    # True

# Verificar se o valor passado existe no dicionário
contatos = {'Yan': '1234-5678', 'John': '3267-1855'}
print('1234-5678' in contatos.values())     # True

# Adicionar valor a um dicionário
contatos['Maria'] = '8888-7777'
print(contatos)

# del
# Remover itens dicionários
del contatos['Maria']
print(contatos)

# pop
# Remove o elemento com a chave especificada e retorna o valor,
# aínda podemos definir um valor padrão de retorno para caso a chave não seja encontrada
print(contatos.pop('Yan'))
print(contatos.pop('Paulo', 'Não encontrado'))
print(contatos)

# update
# juntando dois dicionários
meus_contatos = {'Yan': '1234-5678', 'Pedro': '9999-9999',
                 'Ana': '8765-4321', 'João': '8887-7778'}
contatos_pedro = {'Yan': '1234-5678', 'Fernando': '4345-5434',
                  'Luiza': '4567-7654'}
meus_contatos.update(contatos_pedro)
print(meus_contatos)
