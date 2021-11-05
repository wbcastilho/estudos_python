# Loops / laços f
"""
    for variavel_temporaria in exemplo_array:
        fazer_algo_aqui_dentro
"""

# Quando o programa descobre a quantidade por você
fotos = ['foto1', 'foto2', 'foto3', 'foto4', 'foto5']
for foto in fotos:
    print(foto)

# Você ja sabe a quantidade de vezes que deve rodar
# Função range roda até o penúltimo número
for volume in range(11):
    print(f'Aumentando o volume para {volume}')

# Passando valor inicial e final para o range
for volume in range(1, 11):
    print(f'Aumentando o volume para {volume}')
