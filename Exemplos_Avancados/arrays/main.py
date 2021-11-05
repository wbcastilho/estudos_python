# Arrays

from array import array
from random import random

# cria um array de números de ponto flutuante com dupla precisão (typecode 'd') a partir de qualquer objeto iterável
# nesse caso é uma expressão geradora
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])   # exibe o último elemento do array

