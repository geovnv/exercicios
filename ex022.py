dig = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maíusculas é: {}' .format(dig.upper()))
print('Seu nome em letras minusculas é: {}' .format(dig.lower()))
print('Seu nome tem {} letras' .format(len(dig)-dig.count(' ')))
print('Seu primeiro nome possui {} letras' .format(dig.find(' ')))

