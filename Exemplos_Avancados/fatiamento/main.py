# Fatiamento

l = [10, 20, 30, 40, 50, 60]
print(l[:2])    # exibir do inicio até a posição 2
print(l[2:])    # exibir a partir da posição 2 em diante
print(l[:3])    # exibir do inicio até a posição 3
print(l[3:])    # exibir a partir da posição 3 em diante


# objetos slice
# você pode usar s[a:b:c] para especificar um salto ou um passo c, fazendo a fatia resutante pular itens

s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])