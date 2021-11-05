# list.sort e a função embutida sorted
# Enquanto o método sorted gera uma nova lista ordenada e mantém a lista original intacta
# o método sort ordena a lista original e retorna None

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))                           # gera uma nova lista de string e ordem alfabética
print(sorted(fruits, reverse=True))             # gera uma nova lista de string com a inversão da ordem alfabética
print(sorted(fruits, key=len))                  # gera uma nova lista de string agora ordenada de acordo com o tamanho
print(sorted(fruits, key=len, reverse=True))    # gera uma nova lista de string agora ordenada de acordo com o tamanho
# e pela ordem alfabética reversa

fruits.sort()   # ordenada a lista in-place e devolve o valor None
print(fruits)   # agora fruits esta ordenada
