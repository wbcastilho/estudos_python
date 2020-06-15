# TOmando decisões

horario = 6

'''if horario < 8:
    print('Loja ainda não abriu')
elif horario > 18:
    print('Loja já fechou')
else:
    print('Loja aberta')'''


# Cenário realista
if horario >= 8 and horario <= 12:
   print('Loja está aberta')
elif horario >= 14 and horario <= 18:
    print('Loja está aberta')
else:
    print('Loja está fechada')