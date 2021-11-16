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

    Percorrer chaves do dicionario
    >>> carros = {1: 'Fusca', 2: 'Gol', 3: 'Corsa'}
    >>> for car in carros.keys():
    ...     print(car)
    1
    2
    3

    Percorrer valores do dicionario
    >>> carros = {1: 'Fusca', 2: 'Gol', 3: 'Corsa'}
    >>> for car in carros.values():
    ...     print(car)
    Fusca
    Gol
    Corsa

    Percorrer chaves e valores do dicionario
    >>> carros = {1: 'Fusca', 2: 'Gol', 3: 'Corsa'}
    >>> for key, car in carros.items():
    ...     print(f'key: {key}, carro: {car}')
    key: 1, carro: Fusca
    key: 2, carro: Gol
    key: 3, carro: Corsa

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

    dict Comprehensions
    >>> DIAL_CODES = [
    ...     (86, 'China'),
    ...     (91, 'India'),
    ...     (1, 'United States'),
    ...     (62, 'Indonesia'),
    ...     (55, 'Brazil'),
    ...     (92, 'Pakistan'),
    ...     (880, 'Bangladesh'),
    ... ]

    >>> country_code = {country: code for code, country in DIAL_CODES}
    >>> print(country_code)
    {'China': 86, 'India': 91, 'United States': 1, 'Indonesia': 62, 'Brazil': 55, 'Pakistan': 92, 'Bangladesh': 880}

    invertendo os pares novamente, com os valores em letras maiúsculas e os itens filtrados com code < 66
    >>> print({code: country.upper() for country, code in country_code.items() if code < 66})
    {1: 'UNITED STATES', 62: 'INDONESIA', 55: 'BRAZIL'}
"""