# Dict Comprehensions

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]   # uma lista de pares pode ser usada diretamente com o construtor dict

country_code = {country: code for code, country in DIAL_CODES}  # neste caso os pares são invertidos; country é a chave e code é o valor
print(country_code)

print({code: country.upper() for country, code in country_code.items() if code < 66}) # invertendo os pares novamente, com os valores em letras maiúsculas e os itens filtrados com code < 66