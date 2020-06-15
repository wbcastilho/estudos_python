# Exceptions
''''try:
    ano_atual = int(input('Qual é o ano atual?'))
except ValueError:
    print('Você deve digitar um número.')'''

'''try:
    print(5/0)
except ZeroDivisionError:
    print('Não é possível divir por 0.')'''

'''try:
    print(5/0)
except:
    print('Ocorreu um erro')
finally:
    print('Usuário x realizou cálculos nos sistema.')'''

# Pass - devolve a execução ao início
for pagina in range(10):
    try:
        print('Buscando informações')
        print(5/0)
    except:
        pass

    

