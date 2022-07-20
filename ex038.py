num1 = int(input('Digite um primeiro valor: '))
num2 = int(input('Agora digite outro valor: '))
if num1 > num2:
    print('O número {} é maior que o {}'.format(num1, num2))
elif num2 > num1:
    print('O número {} é maior que o {}'.format(num2, num1))
elif num1 == num2:
    print('Não existe um número maior, pois os dois são iguais.')

