d = float(input('Digite a distância da sua viagem em km: '))
print('.......Calculando o valor da passagem.......')
v1 = d * 0.50
v2 = d * 0.45
if d <= 200:
    print('O valor referente a {}km será de: R${:.2f}'.format(d, v1))
else:
    print('O valor referente a {}km será de: R${:.2f}'.format(d, v2))
