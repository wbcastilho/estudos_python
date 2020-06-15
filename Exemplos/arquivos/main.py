# Como criar e modificar arquivos
valores_celulares = [850, 2230, 1500, 3500, 5000]

'''
'r' -> Usado para ler algo
'w' -> Usado somente para escrever algo
'r+' -> Usado para ler e escrevere algo
'a' -> Usado para escrever algo
'''
'''with open('valores_celulares.txt', 'w') as arquivo:
    for valor in valores_celulares:
        arquivo.write(str(valor) + '\n')'''

'''with open('valores_celulares.txt', 'a') as arquivo:
    for valor in valores_celulares:
        arquivo.write(str(valor) + '\n')'''
        
'''with open('valores_celulares.txt', 'r') as arquivo:
    for valor in arquivo:
        print(valor)'''

# Se existir o arquivo ele altera senão cria um novo
with open('valores_celulares.txt', 'r+') as arquivo:
    for valor in arquivo:
        print(valor)
    arquivo.write('9000')