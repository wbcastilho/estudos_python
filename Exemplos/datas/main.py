# Datas e Horas

from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

print(datetime(2020,1,15))

data_postagem_foto = datetime.strptime(input('Quando devemos postar essa foto'), '%d/%m/%Y')
print(type(data_postagem_foto))

data_inicio = datetime.now()
data_entrega = datetime(2020,1,15)

prazo_entrega = data_entrega - data_inicio
print(prazo_entrega)