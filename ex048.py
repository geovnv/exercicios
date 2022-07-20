soma = 0
for imp in range(1, 501, 2):
    if imp % 3 == 0:
        soma = soma + imp
print('A soma dos números impares múltiplos de 3 entre 1 e 500 será de {}.'.format(soma))