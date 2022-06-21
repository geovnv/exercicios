num = int(input('Digite o número decimal que deseja converter: '))
print('SEGUE OPÇÕES DE CONVERSÃO LISTADAS ABAIXO:')
print('1: Converter para número BINÁRIO')
print('2: Converter para número OCTAL')
print('3: Converter para número HEXADECIMAL')
base = int(input('Agora digite o número referente a base númerica para conversão: '))
if base == 1:
    binario = bin(num)
    print('O número decimal {} em binário é: {}'.format(num, binario [2:]))
elif base == 2:
    octal = oct(num)
    print('O número decimal {} em octal é: {}'.format(num, octal [2:]))
elif base == 3:
    hexade = hex(num)
    print('O número decimal {} em hexadecimal é: {}'.format(num, hexade [2:]))
else:
    print('Não entendi, favor digitar novamente...')
