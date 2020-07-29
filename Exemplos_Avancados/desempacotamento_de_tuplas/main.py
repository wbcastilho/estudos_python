# Desempacotando tuplas

# Exemplo 1
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates

print(latitude)
print(longitude)


# Exemplo 2
t = (20, 8)
quociente, resto = divmod(*t)
print(quociente)
print(resto)
