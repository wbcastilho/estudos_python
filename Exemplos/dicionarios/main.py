"""
    Dicionários

    Criar dicionário
    >>> pessoa = {'Nome': 'Matheus', 'Idade': 19, 'Altura': 168}
    >>> pessoa
    {'Nome': 'Matheus', 'Idade': 19, 'Altura': 168}

    Criar dicionário por meio de função
    >>> filme = dict(nome="Home-Aranha", ano="2025", nota="8")
    >>> filme
    {'nome': 'Home-Aranha', 'ano': '2025', 'nota': '8'}

    Selecionando valores em um dicionário
    >>> x = {1: 10, 2: 20, 3: 30}
    >>> x[1]
    10
    >>> x.get(1)
    10

    Definir valor default caso não exista ao realizar get
     >>> x = {1: 10, 2: 20, 3: 30}
    >>> x.get(0, 100)
    100

    Verificar se a chave existe no dicionário
    >>> contatos = {'Yan': '1234-5678', 'John': '3267-1855'}
    >>> 'Yan' in contatos
    True

    Adicionar valor a um dicionário
    >>> contatos['Maria'] = '8888-7777'
    >>> contatos
    {'Yan': '1234-5678', 'John': '3267-1855', 'Maria': '8888-7777'}

    del - Remover itens dicionários
    >>> del contatos['Maria']
    >>> contatos
    {'Yan': '1234-5678', 'John': '3267-1855'}

    pop - Remove o elemento com a chave especificada e retorna o valor, aínda podemos definir um valor padrão de
    retorno para caso a chave não seja encontrada
    >>> contatos.pop('Yan')
    '1234-5678'
    >>> contatos
    {'John': '3267-1855'}
    >>> contatos.pop('Paulo', 'Não encontrado')
    'Não encontrado'

    update - juntando dois dicionários
    >>> meus_contatos = {'Yan': '1234-5678', 'Pedro': '9999-9999'}
    >>> contatos_pedro = {'Juca': '1234-5678', 'Fernando': '4345-5434'}
    >>> meus_contatos.update(contatos_pedro)
    >>> meus_contatos
    {'Yan': '1234-5678', 'Pedro': '9999-9999', 'Juca': '1234-5678', 'Fernando': '4345-5434'}
"""