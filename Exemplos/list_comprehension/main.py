# List Comprehension
texto = "Morango do Nordeste"

print([letra for letra in texto])

# List Comprehension com condicionais
numeros = range(0, 35)

print([numero for numero in numeros if numero % 2 == 0]) 
print([numero + (numero * 2) for numero in numeros if numero % 2 == 0]) 

numbers = [1, 2, 3, 4, 5]
texto = "ABCDE"

print([(numero, letra) for letra in texto for numero in numeros])