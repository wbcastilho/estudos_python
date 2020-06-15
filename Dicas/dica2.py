# Evitar deixar arquivos abertos
# Códigos somente exemplo

# Maneira errada onde oarquivo fica aberto
data = open("~/Documents/data.csv")
do_something(data)

# Fechando o arquivo
data = open("~/Documents/data.csv")
do_something(data)
data.close()

# Maneira ideal usando um gerenciador de contexto (with)
with open("~/Documents/data.csv") as data:
    do_something(data)