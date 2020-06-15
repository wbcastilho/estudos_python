# Functions

def Logar(usuario, senha):
    print(f'Logando com o usuário {usuario}')
    print(f'Logando com a senha {senha}')

Logar('welber', '1234')

def calcular_preco_cinema(preco_bilhete, multiplicador):
    return preco_bilhete * multiplicador

x = calcular_preco_cinema(10, 2)
print(x) 