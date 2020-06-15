# Strings
nome = 'Guitarra Elétrica'
nome = "Guitarra Elétrica"
print(nome)

# Caracteres de Scape
resenha1 =  "O filme foi \"demais\""
resenha2 =  "O filme foi \'demais\'"
resenha3 =  "O filme foi \ndemais"
caminhos_no_windows = 'meu computador\\fotos\\minhas fotos'
print(resenha1)
print(resenha2)
print(resenha3)
print(caminhos_no_windows)

# Formatando String
aluno = 'Rafael'
nome_do_curso = 'Fotografia'
mensagem = f'Bem vindo ao curso de {nome_do_curso} {aluno}'
print(mensagem)

# Métodos comuns de string
nome_curso = "Edição de vídeo"
print(nome_curso.upper())
print(nome_curso.lower())
print(nome_curso.strip())
print(nome_curso.lstrip())
print(nome_curso.rstrip())
print(nome_curso.find('ção'))  
print(nome_curso.replace('vídeo', 'música'))  
print('https://sc.olx.com.br/?o=90&q=relogio'.replace('relogio','carro'))

# Acessando parte de uma string
mouse = 'Mouse'
print(mouse[3])

descricao = "Esse é um computador que foi ançado e chegou para revolucionar o mercado atual."
print(descricao[-1])
print(descricao.index('o'))

link = "facebook.com/teste"
print(link[0])
print(link[-1])
print(link[0:5])
print(link[1:])
print(link[-5:])
print(link[:-3])