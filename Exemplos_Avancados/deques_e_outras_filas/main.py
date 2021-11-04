# trabalhando com um deque

from collections import deque

dq = deque(range(10), maxlen=10)    # o argumento maxlen opcional define o número máximo de itens permitido nessa instância de deque; isso define um atributo de instância maxlen somente para leitura
print(dq)

dq.rotate(3)    # fazer a rotação com n > 0 retira os itens da extremidade direita e os insere na esquerda; quando n < 0, os itens serão retirados da esquerda e concatenados à direita
print(dq)

dq.rotate(-4) 
print(dq)

dq.appendleft(-1)   # concatenar em um deque que esteja cheio faz com que os itens da outra extremidade sejam descartados
print(dq)

dq.extend([11, 22, 33]) # adicionar três itens a direita e remove três itens a esquerda
print(dq)

dq.extendleft([10, 20, 30, 40]) # faz a adição sucessiva de cada item no argumento iter à esquerda do deque; deste modo, a posição final dos itens estará invertida
print(dq)
