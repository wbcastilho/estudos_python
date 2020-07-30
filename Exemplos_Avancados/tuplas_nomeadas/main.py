# Tuplas nomeadas

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates') # dois parâmetros são necessários para criar uma tupla nomeada: um nome de classe e uma lista de nomes de campos especificados como um interável de strings ou uma única string delimitada por espaços
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))    # os dados devem ser passados como argumentos posicionais ao construtor
print(tokyo)    
print(tokyo.population) # você pode acessar so campos por nome
print(tokyo.coordinates)
print(tokyo[1]) # você também pode acessar os campos por posição

# Atributos e métodos de uma tupla nomeada
print(City._fields) # _fields() retorna uma tupla com os nomes dos campos da classe
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)  # _make() permite instanciar uma tupla nomeada a partir de um interável 
print(delhi._asdict()) 

for key, value in delhi._asdict().items():
    print(key + ':', value)