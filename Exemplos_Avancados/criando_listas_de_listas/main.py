# Criando listas de listas

# uma lista de três listas de tamanho 3 pode representar um tabuleiro de jogo da velha
board = [['_'] * 3 for i in range(3)]  # cria uma lista de três listas com três items cada
print(board)

board[1][2] = 'X'   # coloca uma marca na linha 1 coluna 2
print(board)

# uma lista com três referências à mesma lista é inútil
weird_board = [['_'] * 3] * 3   # a lista externa é composta de três referências à mesma lista interna
print(weird_board)

weird_board[1][2] = '0' # colocar uma marca na linha 1, coluna 2 mostra que todas as linhas são aliases que se referem ao mesmo objeto
print(weird_board)