"""
    Strings

    Formatando String
    >>> aluno = 'Rafael'
    >>> nome_do_curso = 'Fotografia'
    >>> mensagem = f'Bem vindo ao curso de {nome_do_curso} {aluno}'
    >>> mensagem
    'Bem vindo ao curso de Fotografia Rafael'

     Converter para caixa alta
    >>> palavra = 'teste'
    >>> palavra.upper()
    'TESTE'

     Converter para caixa baixa
    >>> palavra = 'TESTE'
    >>> palavra.lower()
    'teste'

    Acessando parte de uma string
    >>> palavra = 'Mouse'
    >>> palavra[3]
    's'

    Converter Lista para String
    >>> palavra = ''.join(['b', 'a', 'n', 'a', 'n', 'a'])
    >>> palavra
    'banana'
    >>> palavra2 = '-'.join(['b', 'a', 'n', 'a', 'n', 'a'])
    >>> palavra2
    'b-a-n-a-n-a'

    Retorna a posição do caracter
    >>> frase = "Esse é o teste"
    >>> frase.index('o')
    7

    Replace
    >>> frase = "Esse é o teste"
    >>> frase.replace('teste', 'novo')
    'Esse é o novo'

    Removendo espaços
    >>> frase = '        banana     '
    >>> frase.strip()
    'banana'

    Posição da string onde inicia o texto passado como parametro
    >>> frase = "Esse é o teste"
    >>> frase.find('teste')
    9

    Pega última letra da string
    >>> link = "facebook.com/teste"
    >>> link[-1]
    'e'

    Retorna da posição 0 a posição 5 da string
    >>> link[0:5]
    'faceb'

    Retorna da posição 1 até o final da string
    >>> link[1:]
    'acebook.com/teste'

    Retorna os ultimos 5 caracteres da string
    >>> link[-5:]
    'teste'

    Retorna do inicio da string até o inicio dos ultimos 3 carcateres
    >>> link[:-3]
    'facebook.com/te'

    Inverter string
    >>> frase = "Esse é o teste"
    >>> frase[::-1]
    'etset o é essE'

    Sorted - Retorna um lista ordenado
    >>> palavra = 'banana'
    >>> palavra_ordenada = sorted(palavra)
    >>> palavra_ordenada
    ['a', 'a', 'a', 'b', 'n', 'n']
"""


